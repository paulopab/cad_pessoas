from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255, null=True, blank=True)
    ativa = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True)

    def __str__(self) -> str:
        return self.nome_completo
