from django import forms
from myapp.models import Human

class HumanForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Human
        fields = ['name', 'age', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'age': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("Возраст не может быть отрицательным.")
        return age