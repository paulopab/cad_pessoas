from django.urls import  path
from .views import ListaPessoaview, PessoaCreateView

urlpatterns = [
    path('', ListaPessoaview.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo')


]