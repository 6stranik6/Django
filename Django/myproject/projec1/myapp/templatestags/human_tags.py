from django import template
from myapp import Profession

register = template.Library()

@register.simple_tag
def get_all_professions():
    return Profession.objects.all()