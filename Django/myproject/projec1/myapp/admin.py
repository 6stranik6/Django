from django.contrib import admin
from .models import Human

class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'gender', 'occupation', 'birth_date', 'created_at', 'first_name', 'last_name', 'profession']
    list_filter = ['gender', 'occupation', 'profession']
    search_fields = ['name', 'occupation', 'first_name', 'last_name']