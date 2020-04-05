from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)

from .models import Aluno



def pesq_list(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        aluno = Aluno.objects.all()
        aluno = aluno.filter(nome__icontains=busca)

    else:
         aluno = Aluno.objects.all().order_by('nome')
         paginator = Paginator(aluno, 6)
         try:
             page = int(request.GET.get('page', '1'))
         except ValueError:
             page = 1

         try:
             aluno = paginator.page(page)
         except (EmptyPage, InvalidPage):
             aluno = paginator.page(paginator.num_pages)

    return render(request,'lista.html', {"aluno":aluno})


# Outra forma de listagem com o ListView
class AlunosList(ListView):
    model = Aluno
    paginate_by = 7

class AlunoEdit(UpdateView):
    model = Aluno
    fields = ['nome', 'cpf', 'identidade', 'email', 'telefone', 'endereco', 'cidade', 'estado', 'plano']

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('list_alunos')

class AlunoNovo(CreateView):
    model = Aluno
    fields = ['nome', 'cpf', 'identidade', 'email', 'telefone', 'endereco', 'cidade', 'estado', 'plano']





