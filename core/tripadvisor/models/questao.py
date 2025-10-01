from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator
from tripadvisor.enumerate import Status
from .perfil import Perfil

class Questao(BaseModel):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    texto = models.TextField(validators=[MinLengthValidator(50)])
    status = models.CharField(max_length= 14,choices=Status, default=Status.NOT_ANSWERED)
    data = models.DateField(auto_now_add=True)
    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo