from django.contrib import admin
from django.db import models
from django.shortcuts import render

class Profession(models.Model):
    name = models.CharField(max_length=100)
    
class Human(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, default='Unspecified')
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['last_name', 'first_name'] 

def human_list(request):
    humans = Human.objects.all()
    professions = Profession.objects.all()  # Получаем все объекты Profession
    return render(request, 'human_list.html', {'humans': humans, 'professions': professions})
    