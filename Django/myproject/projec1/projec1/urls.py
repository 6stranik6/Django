from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import HumanCreateView, ProfessionDetailView, ProfessionCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('humans/', views.human_list, name='human_list'),
    path('humans/create/', HumanCreateView.as_view(), name='human_create'),
    path('professions/', views.professions_list, name='profession_list'),
    path('profession/<int:pk>/', views.get_profession, name='get_profession'),
    path('professions/<int:pk>/', ProfessionDetailView.as_view(), name='profession_detail'),
    path('professions/create/', ProfessionCreateView.as_view(), name='profession_create'),
    path('add_human/', views.add_human, name='add_human'),
]