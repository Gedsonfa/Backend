from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Tarefa

from datetime import datetime


class TarefaAPITestCase(APITestCase):
    def setUp(self):
        # Criando um objeto de Tarefa para o teste
        self.objeto = Tarefa.objects.create(
            tarefa_titulo="Título da tarefa",  # Valor do título da tarefa
            tarefa_descricao="Descrição detalhada da tarefa"  # Valor da descrição
        )

        self.url_get = reverse('get_all_tarefas')  # URL para listar todas as tarefas
        self.url_data = reverse('tarefa_data')  # URL para um recurso específico (detalhes)

        # URL PATCH com o título da tarefa para atualizar
        self.url_patch = reverse('tarefa_detail', args=[self.objeto.tarefa_titulo])

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
        response = self.client.post(self.url_data, data, format="json")

        # Verificando se a resposta é 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando se a nova tarefa foi criada corretamente
        self.assertEqual(response.data['tarefa_titulo'], "Teste3")
        self.assertEqual(response.data['tarefa_descricao'], "É uma tarefa teste")
        self.assertEqual(response.data['tarefa_prazo'], "2025-03-28")
        self.assertEqual(response.data['tarefa_dataConclusao'], "2025-03-28")
        self.assertEqual(response.data['tarefa_situacao'], "Nova")

    def test_delete_tarefa(self):
        # URL genérica de exclusão (sem ID na URL)
        url_delete = reverse('tarefa_data')

        # Enviando DELETE com o ID no corpo da requisição
        data = {"id": self.objeto.id}
        response = self.client.delete(url_delete, data, format="json")

        # Verificando se a resposta é 204 No Content (exclusão bem-sucedida)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificando se a tarefa foi realmente removida do banco de dados
        self.assertFalse(Tarefa.objects.filter(id=self.objeto.id).exists())

    def test_patch_update_tarefa(self):
        # Dados para atualização parcial (todos os campos)
        data = {
            "tarefa_titulo": "Título da tarefa",  # Não modificando o título
            "tarefa_descricao": "Nova descrição atualizada",  # Atualizando descrição
            "tarefa_prazo": "2025-03-28",  # Garantir que o prazo não será alterado
            "tarefa_dataConclusao": "2025-03-28",  # Garantir que a data de conclusão não será alterada
            "tarefa_situacao": "Nova"  # Garantir que a situação não será alterada
        }

        # Fazendo a requisição PATCH para atualizar a descrição da tarefa
        response = self.client.patch(self.url_patch, data, format="json")

        # Verificando se o status da resposta é 202 Accepted (sucesso na atualização)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Obtendo a tarefa atualizada do banco de dados
        self.objeto.refresh_from_db()

        # Verificando se o campo 'tarefa_descricao' foi atualizado corretamente
        self.assertEqual(self.objeto.tarefa_descricao, "Nova descrição atualizada")

        # Convertendo a string para datetime.date para comparação
        expected_date = datetime.strptime("2025-03-28", "%Y-%m-%d").date()

        # Verificando se os outros campos não foram modificados
        self.assertEqual(self.objeto.tarefa_titulo, "Título da tarefa")
        self.assertEqual(self.objeto.tarefa_prazo, expected_date)  # Comparando com datetime.date
        self.assertEqual(self.objeto.tarefa_dataConclusao, expected_date)  # Comparando com datetime.date
        self.assertEqual(self.objeto.tarefa_situacao, "Nova")

    #Exeção
    def test_post_create_tarefa_sem_titulo(self):
        # Dados para criar a tarefa, mas sem o campo 'tarefa_titulo'
        data = {
            "tarefa_descricao": "Descrição detalhada da tarefa",
            "tarefa_prazo": "2025-03-28",
            "tarefa_dataConclusao": "2025-03-28",
            "tarefa_situacao": "Nova"
        }

        # Enviando a requisição POST
        response = self.client.post(self.url_data, data, format="json")

        # Verificando se a resposta é 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verificando se a tarefa não foi criada no banco de dados
        self.assertEqual(Tarefa.objects.count(), 0)