from django.db import models
from django.urls import reverse



class Aluno(models.Model):
    PLANO_CHOICES = (
        ("1", "Plano mensal"),
        ("2", "Plano anual"),
    )

    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    identidade = models.CharField(max_length=9)
    email = models.CharField(max_length=70)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=70)
    cidade = models.CharField(max_length=15)
    estado = models.CharField(max_length=10)
    plano = models.CharField(max_length=1, choices=PLANO_CHOICES, blank=False, null=False)


# property  é uma função interna que cria (adiciona) e retorna  um objeto de propriedade (registro criado)
    @property
    def get_absolute_url(self):
        return reverse('list_alunos')


    def __str__ (self):
        return self.nome



'''o PROTECT não deixa deletar O ALUNO caso o usuario for deletado'''
