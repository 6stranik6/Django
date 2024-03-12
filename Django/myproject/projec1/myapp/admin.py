from django.contrib import admin
from .models import Human, Profession
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class HumanAdminForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            #'age': CKEditorUploadingWidget(),
            # Добавьте CKEditorUploadingWidget к другим полям, если необходимо
        }

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    form = HumanAdminForm

admin.site.register(Profession)