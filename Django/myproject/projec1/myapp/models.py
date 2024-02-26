from django.contrib import admin
from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=100)

class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, default='Unspecified')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['last_name', 'first_name']

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'gender', 'occupation', 'birth_date', 'created_at', 'first_name', 'last_name', 'profession']
    list_filter = ['gender', 'occupation', 'profession']
    search_fields = ['name', 'occupation', 'first_name', 'last_name', 'profession__name']