from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tarefa


class TarefaAPITestCase(APITestCase):
    def setUp(self):
        # Criando um objeto de Tarefa para o teste
        self.objeto = Tarefa.objects.create(
            tarefa_titulo="Título da tarefa",  # Valor do título da tarefa
            tarefa_descricao="Descrição detalhada da tarefa"  # Valor da descrição
        )
        self.url = reverse('get_all_tarefas')  # URL para listar todas as tarefas
        self.url_detail = reverse('tarefa_detail', args=[self.objeto.id])  # URL para um recurso específico (detalhes)

    def test_get_lista_tarefas(self):
        # Fazendo uma requisição GET para obter a lista de tarefas
        response = self.client.get(self.url, format="json")

        # Verificando se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Garante que a resposta é uma lista
        self.assertIsInstance(response.data, list)

        # Verifica se há pelo menos 1 tarefa na resposta
        self.assertGreaterEqual(len(response.data), 1)

        # Verifica se o título da tarefa criada está presente na resposta
        self.assertEqual(response.data[0]['tarefa_titulo'], "Título da tarefa")  # O título da tarefa que foi criado
