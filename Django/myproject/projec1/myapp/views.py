from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Profession
from .models import Human

def my_custom_404_view(request, exception):
    return render(request, '404/404.html', status=404)

def human_list(request):
    humans = Human.objects.all()
    professions = Profession.objects.all()
    return render(request, 'myapp/human_list.html', {'humans': humans, 'professions': professions})

def professions_list(request):
    professions = Profession.objects.all()
    return render(request, 'myapp/professions_list.html', {'professions': professions})

def get_profession(request, profession_id):
    profession = Profession.objects.get(id=profession_id)
    humans_with_profession = Human.objects.filter(profession=profession)
    
    return render(request, 'myapp/professions_list.html', {
        'profession': profession,
        'humans_with_profession': humans_with_profession,
    })