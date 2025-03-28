from django.core.management.base import BaseCommand
from api_rest.models import Tarefa
from faker import Faker
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Cria 15 tarefas com prazos, datas e situações variadas'

    def handle(self, *args, **kwargs):
        fake = Faker()
        situacoes = ["Nova", "Em andamento", "Concluída", "Cancelada"]
        created_tasks = []

        for _ in range(15):
            # Gerar dados falsos para a tarefa
            titulo = fake.sentence(nb_words=4)
            descricao = fake.paragraph(nb_sentences=2)
            prazo = fake.date_this_year(before_today=True, after_today=False)  # Prazo no passado
            data_conclusao = prazo + timedelta(days=random.randint(1, 10))  # Data de conclusão dentro de 1-10 dias após o prazo
            situacao = random.choice(situacoes)  # Escolher uma situação aleatória

            # Criar a tarefa
            tarefa = Tarefa.objects.create(
                tarefa_titulo=titulo,
                tarefa_descricao=descricao,
                tarefa_prazo=prazo,
                tarefa_dataConclusao=data_conclusao,
                tarefa_situacao=situacao
            )

            created_tasks.append(tarefa)

        self.stdout.write(self.style.SUCCESS(f'{len(created_tasks)} tarefas criadas com sucesso!'))
