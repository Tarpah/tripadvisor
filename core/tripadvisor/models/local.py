from .atracao import Atracao
from tripadvisor.enumerate import Classificacao

from django.db import models
from ..managers import LocalManager
from django.core.validators import MinValueValidator


class Local(Atracao):
    horario_abertura = models.DateTimeField()
    horario_fechamento = models.DateTimeField()
    acessibilidade = models.BooleanField()
    classificao = models.CharField(max_length=13, choices=Classificacao, default=Classificacao.GENERAL)

    objects = LocalManager()

    def __str__(self):
        return f'{self.nome} PK:{self.pk}'