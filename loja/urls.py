from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
]