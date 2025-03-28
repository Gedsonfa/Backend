from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa
from .serializers import TarefaSerializer

import json

# Create your views here.

@api_view(['GET'])
def get_tarefas(request):

    if request.method == 'GET':

        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Metodos por URLs
@api_view(['GET', 'PUT'])
def get_by_titulo(request, titulo):

    try: 
        tarefa = Tarefa.objects.get(tarefa_titulo=titulo)
    except:
        return Response(sattus=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)
    
    if request.method == 'PUT':

        serializer = TarefaSerializer(tarefa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
#CRUD 
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tarefa_manager(request):
    if request.method == 'GET':
        tarefa_titulo = request.GET.get('tarefa')  # Obter o título da tarefa
        if tarefa_titulo:
            try:
                tarefa = Tarefa.objects.get(tarefa_titulo=tarefa_titulo)
            except Tarefa.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        else:
            tarefas = Tarefa.objects.all()
            serializer = TarefaSerializer(tarefas, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        new_tarefa = request.data
        serializer = TarefaSerializer(data=new_tarefa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        tarefa_titulo = request.data.get('tarefa_titulo')
        try:
            tarefa = Tarefa.objects.get(tarefa_titulo=tarefa_titulo)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarefa_titulo = request.data.get('tarefa_titulo')
        try:
            tarefa = Tarefa.objects.get(tarefa_titulo=tarefa_titulo)
            tarefa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
def tarefa_list(request):
    tarefa_list = Tarefa.objects.all()

    paginator = Paginator(tarefa_list, 5) #numero de objetos por pag

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj' : page_obj})
def tarefa_search(request):
    search = request.GET.get('search', '')  # Obtém o termo de busca
    tarefas = Tarefa.objects.all()  # Busca todas as tarefas inicialmente

    if search:
        tarefas = tarefas.filter(
            Q(tarefa_titulo__icontains=search) | Q(tarefa_descricao__icontains=search)
        )

    return render(request, "list.html", {"page_obj": tarefas, "search": search})