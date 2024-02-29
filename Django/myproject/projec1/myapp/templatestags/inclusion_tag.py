from django import template
from myapp.models import Profession  # <--- Подставьте соответствующую модель для профессий

register = template.Library()

@register.inclusion_tag('professions_list.html')
def show_professions_list():
    professions = Profession.objects.all()
    return {'professions': professions}