import pessoa
from django import  forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
 class Meta:
    models = Pessoa
    fields = ['nome_completo', 'data_nascimento', 'ativa']