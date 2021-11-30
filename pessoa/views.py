from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Pessoa
from .forms import PessoaForm


# Classe para criação de listagem de pesoas
class ListaPessoaview(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('id')


# Classe para ciação de formulários
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'
