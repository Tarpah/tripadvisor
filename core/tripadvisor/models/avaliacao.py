from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

class Avaliacao(BaseModel):
    titulo = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    texto = models.TextField(validators=[MinLengthValidator(50)])
    nota = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    data_visita = models.DateField() # estava data_vista provavelmente errado, perguntar ao professor.
    data_avaliacao = models.DateField(auto_now_add=True) # é automático? perguntar professor
    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    atracao = models.ForeignKey('tripadvisor.Atracao', on_delete=models.RESTRICT)
    perfil = models.ForeignKey('tripadvisor.Perfil', on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo

    class Meta:
        unique_together = ('perfil', 'atracao')

