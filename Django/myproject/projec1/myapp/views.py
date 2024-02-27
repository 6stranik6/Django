from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Profession
from .models import Human

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def human_list(request):
    humans = Human.objects.all()
    return render(request, 'myapp/human_list.html', {'humans': humans})

def professions_list(request):
    professions = Profession.objects.all()
    return render(request, 'myapp/professions_list.html', {'professions': professions})