from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator
from .atracao import Atracao

class Endereco(BaseModel):
    cep = models.CharField(validators=[MinLengthValidator(8)], max_length=8)
    logradouro = models.CharField(validators=[MinLengthValidator(5)], max_length=50)
    numero = models.IntegerField(validators=[MinValueValidator(0)])
    complemento = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    bairro = models.CharField(validators=[MinLengthValidator(5)], max_length=30)
    cidade = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    estado = models.CharField(validators=[MinLengthValidator(5)], max_length=30)
    pais = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    atracao = models.OneToOneField(Atracao, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.cidade}, {self.bairro}, {self.numero}"