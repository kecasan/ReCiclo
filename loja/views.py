from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    # 1. Busca todos os objetos 'Produto' no banco de dados
    produtos = Produto.objects.all()

    # 2. Define o contexto para enviar ao template
    contexto = {
        'produtos': produtos,
    }

    # 3. Renderiza o template com os dados
    return render(request, 'loja/lista_produtos.html', contexto)