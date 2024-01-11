class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node()
            self.root.value = value
            return
        self._add_data(self.root, value)

    def _add_data(self, cn, value):
        if cn.value > value:
            if cn.left is None:
                cn.left = Node()
                cn.left.value = value
                cn.left.parent = cn
            else:
                self._add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = Node()
                cn.right.value = value
                cn.right.parent = cn
            else:
                self._add_data(cn.right, value)
    
    def populate_tree(self, sorted_list):
        if not sorted_list:
            return
        
        mid = len(sorted_list) // 2
        self.add(sorted_list[mid])
        
        left_list = sorted_list[:mid]
        right_list = sorted_list[mid+1:]
        
        self.populate_tree(left_list)
        self.populate_tree(right_list)
    
    def find(self, value):
        if self.root is None:
            return False
        if self.root.value == value:
            return True
        
        node = self._find_node(self.root, value)
        if node is None:
            return False
        
        return True
    
    def _find_node(self, cn, value):
        if cn is None:
            return None
        
        if cn.value == value:
            return cn
        
        if cn.value > value:
            return self._find_node(cn.left, value)
        else:
            return self._find_node(cn.right, value)
        
    def find_min(self):
        return self._find_min_node(self.root).value
    
    def _find_min_node(self, cn):
        if cn.left is None:
            return cn
        
        return self._find_min_node(cn.left)
    
    def find_max(self):
        return self._find_max_node(self.root).value
    
    def _find_max_node(self, cn):
        if cn.right is None:
            return cn
        
        return self._find_max_node(cn.right)
    
    def delete(self, value):
        if self.root is None:
            return
        
        if self.root.value == value and self.root.left is None and self.root.right is None:
            self.root = None
            return
        
        node = self._find_node(self.root, value)
        if node is None:
            raise Exception("Cannot find node to delete")
        
        self._delete_node(node)
    
    def _delete_node(self, node):
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is not None and node.right is None:
            if node.parent.left == node:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        elif node.left is None and node.right is not None:
            if node.parent.left == node:
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
        else:
            min_node_of_right = self._find_min_node(node.right)
            node.value = min_node_of_right.value
            self._delete_node(min_node_of_right)
    

# Example usage
bst = BinarySearchTree()
values = [1, 3, 5, 6, 7, 8, 15, 19, 22]
bst.populate_tree(values)

print(bst.find(3))  
print(bst.find(10))  

bst.delete(5)
print(bst.find(5))  
print(bst.find_min())  
print(bst.find_max())  
