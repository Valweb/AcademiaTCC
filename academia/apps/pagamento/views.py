import csv
import xlwt
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Pagamento
from .models import Aluno


class PagamentosList(ListView):
      model = Pagamento
      paginate_by = 2

class DadosAluno(DetailView):
      model = Aluno
      template_name = 'pagamento/pagamento_detail.html'

class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contas_receber.csv"'

        pagamentos = Pagamento.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Matricula', 'Nome', 'CPF', 'Tetefone', 'Vencimanto'])

        for pagamento in pagamentos:
            writer.writerow([pagamento.aluno.matricula,
                             pagamento.aluno.nome,
                             pagamento.aluno.cpf,
                             pagamento.aluno.telefone,
                             pagamento.vencimento
                             ])

        return response

class ExportarExcel(View):
    def get (self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="contas_receber.xls"'
        
        wb = xlwt.Workbook(encoding='uft-8')
        ws = wb.add_sheet('Alunos inadiplentes')

        row_num = 0

        columns = ['Matricula', 'Nome', 'CPF', 'Tetefone', 'Vencimanto' ]
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])
            

        pagamentos = Pagamento.objects.all()
        
        row_num = 1
        for pagamento in pagamentos:
            ws.write(row_num, 0, pagamento.aluno.matricula)
            ws.write(row_num, 1, pagamento.aluno.nome)
            ws.write(row_num, 2, pagamento.aluno.cpf)
            ws.write(row_num, 3, pagamento.aluno.telefone)
            ws.write(row_num, 4, pagamento.vencimento)
            row_num += 1

        wb.save(response)
        return response
            