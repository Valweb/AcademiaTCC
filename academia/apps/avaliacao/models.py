from django.db import models
from apps.aluno.models import Aluno

class avaliacao(models.Model):
    matricula = models.ForeignKey(
        Aluno, on_delete=models.PROTECT)
    anamnese = models.CharField(max_length=100, help_text='Anamnese')
    dobras = models.CharField(max_length=100, help_text='Dobras')
    ergometrico = models.CharField(max_length=100, help_text='Ergométrico')
    data_avaliacao = models.DateField(null=True)
    data_notifica = models.DateField(null=True)

