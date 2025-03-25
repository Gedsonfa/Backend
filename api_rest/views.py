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