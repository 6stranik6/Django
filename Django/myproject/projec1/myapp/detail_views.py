from myapp.views import DetailView
from myapp.views import professions_list

class ProfessionDetailView(DetailView):
    model = professions_list
    template_name = 'myapp/profession_detail.html'
    context_object_name = 'profession'