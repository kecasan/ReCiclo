from django.shortcuts import render
from .models import Noticia

def lista_noticias(request):
    #1. Buscar todos os objetos 'Noticia' no banco de dados
    todas_as_noticias = Noticia.objects.all().order_by('-data_publicacao')
    
    #2. Definir o 'contexto'que será enviado para o template
    contexto ={
        'noticias': todas_as_noticias,
    }

    #3. Renderizar o template HTML com os dados do contexto
    return render(request, 'noticias/lista_noticias.html', contexto)
