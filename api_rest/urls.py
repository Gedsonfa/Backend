from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_tarefas, name='get_all_tarefas'),
    path('tarefa/<str:titulo>', views.get_by_titulo, name='tarefa_detail'),
    path('tarefa/id/<int:id>', views.get_by_titulo, name='tarefa_detail_by_id'),
    path('buscar/', views.tarefa_search, name='tarefa_search'),
    path('data/', views.tarefa_manager, name='tarefa_data'),
    path('planilha/', views.tarefa_list, name='tarefa_list'),
]   