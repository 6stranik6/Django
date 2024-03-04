from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('humans/', views.human_list, name='human_list'),
    path('professions/', views.professions_list, name='profession_list'),
    path('profession/<int:pk>/', views.get_profession, name='get_profession'),
    path('profession/<int:pk>/', views.profession_detail, name='profession_detail'),
    path('add_human/', views.add_human, name='add_human'),
]