from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Atracao(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5, 'O nome deve conter no minimo 5 caracteres')])

    nota = models.DecimalField(max_digits=3, max_length=3)
    ingresso = models.BooleanField()
    valor = models.
