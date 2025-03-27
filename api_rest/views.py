from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa
from .serializers import TrefaSerializer

import json

# Create your views here.

@api_view(['GET'])
def get_tarefas(request):

    if request.method == 'GET':

        tarefas = Tarefa.objects.all()

        serializer = TrefaSerializer(tarefas, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_titulo(request, titulo):

    try: 
        tarefa = Tarefa.objects.get(pk=titulo)
    except:
        return Response(sattus=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = TrefaSerializer(tarefa)
        return Response(serializer.data)

#CRUD 
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tarefa_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['tarefa']:

                tarefa_titulo = request.GET['tarefa']

                try:
                    tarefa = Tarefa.objects.get(pk=tarefa_titulo)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = TrefaSerializer(tarefa)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Criando dados
    if request.method == 'POST':

        new_tarefa = request.data

        serializer = TrefaSerializer(data=new_tarefa)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #EDITAR DADOS (PUT)
    if request.method == 'PUT':

        tarefa_titulo = request.data['tarefa_titulo']

        try:    
            update_tarefa = Tarefa.objects.get(pk=tarefa_titulo)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)

        serializer = TrefaSerializer(update_tarefa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)