from django.urls import  path
from .views import ListaPessoaview

urlpatterns = [
    path('', ListaPessoaview.as_view(), name='pessoa.index')
]