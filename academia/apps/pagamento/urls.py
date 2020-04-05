from django.urls import path
from .views import PagamentosList, DadosAluno, ExportarParaCSV, ExportarExcel


urlpatterns = [
     path('', PagamentosList.as_view(), name="list_pagamentos"),
     path('detalhes/<int:pk>/', DadosAluno.as_view(), name="dados"),
     path('exportar-csv', ExportarParaCSV.as_view(), name="csv"),
     path('exportar-excel', ExportarExcel.as_view(), name="excel"),
]

