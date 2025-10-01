from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator
from tripadvisor.enumerate import Proposito, Transporte

class Viagem(BaseModel):
    titulo = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    descricao = models.TextField(null=True, blank=True)
    destino = models.TextField(validators=[MinLengthValidator(3)], max_length=100, null=True, blank=True)
    pais_destino = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    inicio = models.DateField(auto_now_add=True) # Adicionar mais tarde o Final
    orcamento = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    proposito = models.CharField(max_length=9, choices=Proposito, default=Proposito.OUTRO)
    notas = models.TextField(blank=True, null=True)
    transporte = models.CharField(max_length=8, choices=Transporte, default=Transporte.SEVERAL)

    def __str__(self):
        return self.titulo