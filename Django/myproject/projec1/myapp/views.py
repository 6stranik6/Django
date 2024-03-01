from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from myapp.models import Profession
from myapp.models import Human
from django.views.generic.detail import DetailView 

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
    profession = Profession.objects.get(id=profession_id)
    humans_with_profession = Human.objects.filter(profession=profession)
    
    return render(request, 'myapp/profession_detail.html', {
        'profession': profession,
        'humans_with_profession': humans_with_profession,
    })

def profession_detail(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    return render(request, 'myapp/profession_detail.html', {'profession': profession})