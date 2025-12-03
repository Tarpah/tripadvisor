from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator

from tripadvisor.enumerate import Classificacao
from ..managers import CategoriaManager

class Categoria(BaseModel):
    nome = models.CharField(validators=[MinLengthValidator(5)], max_length=50)
    classificacao = models.CharField(max_length=8, choices=Classificacao, default=Classificacao.GENERAL)
    descricao = models.TextField()

    objects = CategoriaManager()

    def __str__(self):
        return f'{self.nome} PK:{self.pk}'