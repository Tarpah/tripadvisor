from tkinter.constants import CASCADE

from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.timezone import now
from django.core.validators import ValidationError
from tripadvisor.enumerate import Proposito, Transporte
from tripadvisor.models.perfil import Perfil


class Viagem(BaseModel):
    titulo = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    descricao = models.TextField(null=True, blank=True)
    destino = models.TextField(validators=[MinLengthValidator(3)], max_length=100, null=True, blank=True)
    pais_destino = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    inicio = models.DateField(default=now, verbose_name='Data do inicio da viagem')
    final = models.DateField(default=now, verbose_name='Data do fim da viagem')
    orcamento = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)   ])
    proposito = models.CharField(max_length=9, choices=Proposito, default=Proposito.OUTRO)
    notas = models.TextField(blank=True, null=True)
    transporte = models.CharField(max_length=8, choices=Transporte, default=Transporte.SEVERAL)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def clean(self):
        try:
            if self.inicio > self.final:
                raise ValidationError('A data do fim da viagem deve ser depois da data de inicio da viagem.')

        except ValueError:
            pass