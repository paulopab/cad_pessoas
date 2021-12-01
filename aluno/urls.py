from django.urls import path
from .views import ListAlunoView
urlpatterns = [
    path('', ListAlunoView.as_view(), name='aluno.index')
]