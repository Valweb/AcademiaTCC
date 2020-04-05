from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user.username
    return render(request, 'inicio/index.html', data)


# com login required o usuário é obrigado estar logado para acessar essa url