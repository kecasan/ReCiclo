# contas/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class cadastro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redireciona para a página de login após o sucesso
    template_name = 'registration/cadastro.html'