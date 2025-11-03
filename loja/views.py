from django.shortcuts import render, get_object_or_404
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

def detalhe_produto(request, pk):
    # Busca o produto pela pk ou retorna um erro 404
    produto = get_object_or_404(Produto, pk=pk)
    
    contexto = {
        'produto': produto,
    }
    return render(request, 'loja/detalhe_produto.html', contexto)