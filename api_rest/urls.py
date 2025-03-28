from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.tarefa_list, name='tarefa_list'),
    path('tarefa/<str:titulo>', views.get_by_titulo),
    path('buscar/', views.tarefa_search, name='tarefa_search'),
    path('data/', views.tarefa_manager)
]