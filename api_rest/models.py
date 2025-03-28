from django.db import models

# Create your models here.

class Situacao(models.TextChoices):
    NOVA = "Nova", "Nova"
    EM_ANDAMENTO = "Em andamento", "Em andamento"
    CONCLUIDA = "Concluída", "Concluída"
    CANCELADA = "Cancelada", "Cancelada"

class Tarefa(models.Model):
    tarefa_titulo = models.CharField(max_length=100, unique=True)
    tarefa_descricao = models.CharField(max_length=250, default='')
    tarefa_prazo = models.DateField(null=True, blank=True)
    tarefa_dataConclusao = models.DateField(null=True, blank=True)
    tarefa_situacao = models.CharField(
        max_length=20,
        choices=Situacao.choices,
        default=Situacao.NOVA
    )

    def __str__(self):
        return f'Título: {self.tarefa_titulo} | Descrição: {self.tarefa_descricao} | Prazo: {self.tarefa_prazo} | Data Conclusão: {self.tarefa_dataConclusao} | Situação: {self.tarefa_situacao}'