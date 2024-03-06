from django import template
from myapp.models import Profession

register = template.Library()

@register.simple_tag
def professions_with_people():
    professions_with_people = Profession.objects.filter(person__isnull=False).distinct()
    return professions_with_people