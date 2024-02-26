from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Profession

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def professions_list(request):
    professions = Profession.objects.all()
    return render(request, 'professions_list.html', {'professions': professions})