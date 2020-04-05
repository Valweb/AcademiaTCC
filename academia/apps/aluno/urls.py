from django.urls import path
from .views import AlunosList
from .views import AlunoEdit
from .views import AlunoDelete
from .views import AlunoNovo
from .views import pesq_list


urlpatterns = [
    path('', AlunosList.as_view(), name='list_alunos'),
    path('novo/', AlunoNovo.as_view(), name='create_aluno'),
    path('editar/<int:pk>/', AlunoEdit.as_view(), name='update_aluno'),
    path('deletar/<int:pk>/', AlunoDelete.as_view(), name='delete_aluno'),
    path('list/', pesq_list,name='lista'),
]
