from django.shortcuts import render, get_object_or_404 # Adicione get_object_or_404
from .models import Noticia

def lista_noticias(request):
    todas_as_noticias = Noticia.objects.all().order_by('-data_publicacao')
    contexto = {
        'noticias': todas_as_noticias,
    }
    return render(request, 'noticias/lista_noticias.html', contexto)

# --- NOSSA NOVA VIEW ---
def detalhe_noticia(request, pk):
    # Busca a notícia com a 'pk' (ID) vinda da URL, ou mostra um erro 404 se não encontrar
    noticia = get_object_or_404(Noticia, pk=pk)
    
    contexto = {
        'noticia': noticia, # Passamos apenas a notícia encontrada
    }
    return render(request, 'noticias/detalhe_noticia.html', contexto)