from django.db import models

# Create your models here.

class Situacao(models.TextChoices):
    PENDENTE = "PEN", "Pendente"
    APROVADO = "APR", "Aprovado"
    REJEITADO = "REJ", "Rejeitado"
    CANCELADO = "CAN", "Cancelado"

class Tarefa(models.Model):

    tarefa_titulo = models.CharField(primary_key=True, max_length=100, default='')
    tarefa_descricao = models.CharField(max_length=250, default='')
    tarefa_prazo = models.DateField(default='')
    tarefa_dataConclusao = models.DateField(default='')
    tarefa_situacao = models.CharField(
        max_length=3,
        choices=Situacao.choices,
        default=''
    )

    def __str__(self):
        return f'Título: {self.tarefa_titulo} | Descrição: {self.tarefa_descricao} | Prazo: {self.tarefa_prazo} | Data Conclusão: {self.tarefa_dataConclusao} | Situação: {self.tarefa_situacao}  '