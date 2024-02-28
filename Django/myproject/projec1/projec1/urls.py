from operator import index
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import human_list

urlpatterns = [
    path('index/', views.index, name='hello_world'),
    path('admin/', admin.site.urls),
    path('humans/', human_list, name='human_list'),
    path('professions/', views.professions_list, name='profession_list'),
    path('profession/<int:profession_id>/', views.get_profession, name='get_profession'),
]