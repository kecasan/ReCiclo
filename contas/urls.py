# contas/urls.py
from django.urls import path
from . import views

app_name = 'contas'

urlpatterns = [
    path('cadastro/', views.cadastro.as_view, name='cadastro'),
]