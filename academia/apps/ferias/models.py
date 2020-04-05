from django.db import models
from apps.aluno.models import Aluno
#from apps.pagamento.models import Pagamento
from datetime import date


class Ferias(models.Model):
    matricula = models.ForeignKey(
        Aluno, on_delete=models.PROTECT)
    dias_acumulados = models.IntegerField(null=True)
    data_inicial = models.DateField()
    data_final = models.DateField()
   # altera = models.ForeignKey(Pagamento, on_delete=models.PROTECT) e for alterar na mão

    def calcula_dias (self, date1, date2):
     d1=date.strptime(date1, "%Y-%m-%d")
     d2=date.strptime(date2, "%Y-%m-%d")
     soma= abs((d1+d2))
     return str(soma)








    # def calcula_venc(self):
        # return self.Pagamento.vencimento +






