from django.urls import path
from . import views

# Damos um 'nome' ao nosso conjunto de urls para organizar melhor
app_name = 'noticias'

urlpatterns = [
    # ex: /noticias/
    path('', views.lista_noticias, name='lista_noticias'),
    
    # ex: /noticias/5/
    path('<int:pk>/', views.detalhe_noticia, name='detalhe_noticia'),
]