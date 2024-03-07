from django.contrib import admin
from .models import Human
from .models import Profession


admin.site.register(Human)
admin.site.register(Profession)