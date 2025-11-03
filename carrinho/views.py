# carrinho/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from loja.models import Produto

@require_POST # Garante que esta view só possa ser acessada via método POST
def adicionar_ao_carrinho(request, produto_id):
    # Primeiro, obtemos o carrinho da sessão, ou criamos um dicionário vazio se ele não existir
    carrinho = request.session.get('carrinho', {})
    
    # Pegamos o produto do banco de dados
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Convertemos o ID para string porque as chaves de sessão são strings
    produto_id_str = str(produto.id)

    # Verificamos se o produto já está no carrinho
    if produto_id_str in carrinho:
        # Se estiver, apenas incrementamos a quantidade
        carrinho[produto_id_str]['quantidade'] += 1
    else:
        # Se não, adicionamos o produto ao carrinho com quantidade 1
        carrinho[produto_id_str] = {
            'quantidade': 1,
            'preco': str(produto.preco),
            'nome': produto.nome,
        }
    
    # Salvamos o carrinho de volta na sessão
    request.session['carrinho'] = carrinho
    
    # Redirecionamos para a página de visualização do carrinho (que faremos a seguir)
    return redirect('carrinho:detalhe_carrinho')

def detalhe_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    contexto = {'carrinho': carrinho}
    return render(request, 'carrinho/detalhe_carrinho.html', contexto)