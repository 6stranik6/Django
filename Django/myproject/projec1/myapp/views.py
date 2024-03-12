from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from myapp.models import Profession, Human
from myapp.forms import HumanForm
from django.urls import reverse
from myapp.mixins import AuthorizeMixin
from django.views.generic.base import View
from django.http import JsonResponse

class HumanListView(ListView):
    model = Human
    template_name = 'myapp/human_list.html'
    context_object_name = 'humans'

    def get_queryset(self):
        return super().get_queryset().select_related('profession')

class ProfessionListView(ListView):
    model = Profession
    template_name = 'myapp/professions_list.html'
    context_object_name = 'professions'
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('human_set')

class CustomProfessionDetailView(DetailView):
    model = Profession
    template_name = 'myapp/profession_detail.html'
    context_object_name = 'profession'

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('human_list')
    else:
        form = HumanForm()
    return render(request, 'add_human.html', {'form': form})

class HumanCreateView(AuthorizeMixin, CreateView):
    model = Human
    template_name = 'myapp/human_form.html'
    fields = '__all__'
    

class ProfessionCreateView(CreateView):
    model = Profession
    template_name = 'myapp/profession_form.html'
    fields = '__all__'

class YourCKEditorUploadView(View):
    def post(self, request, *args, **kwargs):
        # Ваш код для обработки загрузки файла
        return JsonResponse({'url': 'url_to_uploaded_file'})