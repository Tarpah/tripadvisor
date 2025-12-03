from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator
from .perfil import Perfil
from .questao import Questao
from ..managers import RespostaManager

class Resposta(BaseModel):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    texto = models.TextField(validators=[MinLengthValidator(50)])
    data = models.DateField(auto_now_add=True)
    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    objects = RespostaManager()

    def __str__(self):
        return f'{self.titulo} PK:{self.pk}'