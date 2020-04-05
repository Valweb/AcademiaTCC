from django.db import models
from apps.aluno.models import Aluno
from django.db.models.fields import DateField

class Pagamento(models.Model):
    STATUS_CHOICES = (
        ("1", "Pago"),
        ("2", "Aberto"),
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    vencimento = models.DateField(null=True)
    data_baixa = models.DateField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    def __repr__(self):
        return self.vencimento













