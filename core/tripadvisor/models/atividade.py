from .atracao import Atracao
from tripadvisor.enumerate import Turno, Dificuldade

from django.db import models
from django.core.validators import MinValueValidator


class Atividade(Atracao):
    turno = models.CharField(max_length=14, choices=Turno, default=Turno.MORNING)
    duracao = models.TimeField() # conversar com o sor, possivelmente é models.DurationField()
    guia = models.BooleanField()
    participantes = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    dificuldade = models.CharField(max_length=13, choices=Dificuldade, default=Dificuldade.EASY)