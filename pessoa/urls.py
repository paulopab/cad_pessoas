from django.urls import path
from .views import ListaPessoaview, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    path('', ListaPessoaview.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
    path('editar/<int:pk>', PessoaUpdateView.as_view(), name='pessoa.editar'),
    path('excluir/<int:pk>', PessoaDeleteView.as_view(), name='pessoa.excluir'),

]
