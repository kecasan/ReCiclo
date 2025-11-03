# carrinho/urls.py
from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.detalhe_carrinho, name='detalhe_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
]