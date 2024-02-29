from django import template
from myapp.models import Category 

register = template.Library()

@register.simple_tag
def get_category_name(category_id):
    try:
        category = Category.objects.get(id=category_id)
        return category.name
    except Category.DoesNotExist:
        return "No category found"