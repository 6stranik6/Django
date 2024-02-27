from operator import index
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import human_list

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('humans/', human_list, name='human_list'),
    path('professions/', views.professions_list, name='profession_list'),
]