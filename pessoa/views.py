from django.shortcuts import render
# Importação das funções Listagem(ListView), Geração de formulários(CreateView),
# Atualização de registro(UpdateView), Deleção de registro (DeleteView)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm


# Classe para criação de listagem de pesoas
class ListaPessoaview(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('id')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        return queryset


# Classe para criação de formulários
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'

# Classe para edição de pessoas
class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'

# Classe para deleção de pessoas
class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoa/'
