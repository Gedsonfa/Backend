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
        self.url_get = reverse('get_all_tarefas')  # URL para listar todas as tarefas
        self.url_post = reverse('tarefa_data')  # URL para um recurso específico (detalhes)

    def test_get_lista_tarefas(self):
        # Fazendo uma requisição GET para obter a lista de tarefas
        response = self.client.get(self.url_get, format="json")

        # Verificando se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Garante que a resposta é uma lista
        self.assertIsInstance(response.data, list)

        # Verifica se há pelo menos 1 tarefa na resposta
        self.assertGreaterEqual(len(response.data), 1)

        # Verifica se o título da tarefa criada está presente na resposta
        self.assertEqual(response.data[0]['tarefa_titulo'], "Título da tarefa")  # O título da tarefa que foi criado

    def test_post_create_tarefa(self):
        # Criando uma nova tarefa com o método POST
        data = {
            "tarefa_titulo": "Teste3",
            "tarefa_descricao": "É uma tarefa teste",
            "tarefa_prazo": "2025-03-28",
            "tarefa_dataConclusao": "2025-03-28",
            "tarefa_situacao": "Nova"
        }
        response = self.client.post(self.url_post, data, format="json")

        # Verificando se a resposta é 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando se a nova tarefa foi criada corretamente
        self.assertEqual(response.data['tarefa_titulo'], "Teste3")
        self.assertEqual(response.data['tarefa_descricao'], "É uma tarefa teste")
        self.assertEqual(response.data['tarefa_prazo'], "2025-03-28")
        self.assertEqual(response.data['tarefa_dataConclusao'], "2025-03-28")
        self.assertEqual(response.data['tarefa_situacao'], "Nova")