from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)  # Добавлено поле first_name
    last_name = models.CharField(max_length=50)  # Добавлено поле last_name
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['last_name', 'first_name']
