from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from myapp.models import Profession
from myapp.models import Human
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .forms import HumanForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

class ProfessionDetailView(DetailView):
    model = Profession
    template_name = 'myapp/profession_detail.html'
    context_object_name = 'profession'

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
    profession = get_object_or_404(Profession, id=profession_id)
    humans_with_profession = Human.objects.filter(profession=profession)
    
    return render(request, 'myapp/profession_detail.html', {
        'profession': profession,
        'humans_with_profession': humans_with_profession,
    })

def profession_detail(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    return render(request, 'myapp/profession_detail.html', {'profession': profession})

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('human_list'))
    else:
        form = HumanForm()
    return render(request, 'add_human.html', {'form': form})

class HumanListView(ListView):
    model = Human
    template_name = 'myapp/human_list.html'
    context_object_name = 'humans'

class HumanCreateView(CreateView):
    model = Human
    template_name = 'myapp/human_form.html'
    fields = '__all__' 

class ProfessionListView(ListView):
    model = Profession
    template_name = 'myapp/profession_list.html'
    context_object_name = 'professions'

class ProfessionDetailView(DetailView):
    model = Profession
    template_name = 'myapp/profession_detail.html'

class ProfessionCreateView(CreateView):
    model = Profession
    template_name = 'myapp/profession_form.html'
    fields = '__all__' 