from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import HumanCreateView, CustomProfessionDetailView, ProfessionCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('humans/', views.HumanListView.as_view(), name='human_list'),
    path('humans/create/', HumanCreateView.as_view(), name='human_create'),
    path('professions/', views.ProfessionListView.as_view(), name='profession_list'),
    path('professions/<int:pk>/', CustomProfessionDetailView.as_view(), name='profession_detail'),
    path('professions/create/', ProfessionCreateView.as_view(), name='profession_create'),
    path('add_human/', views.add_human, name='add_human'),
]