from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from .categoria import Categoria
from .viagem import Viagem
from .endereco import Endereco

class Atracao(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5, 'O nome deve conter no minimo 5 caracteres')])

    nota = models.FloatField()
    ingresso = models.BooleanField()
    valor = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    informacoes = models.TextField(null=True, blank=True)
    site = models.URLField()
    telefone = models.CharField(max_length=11, null=True, blank=True,
                                validators=[
                                    MinLengthValidator(11, 'Telefone deve ter 11 digitos.')
                                ])
    categorias = models.ManyToManyField(Categoria, blank=True,) # conexão 0 para N
    viagens = models.ManyToManyField(Viagem, blank=True ) # conexão 0 para N
    avaliacoes = models.ManyToManyField('tripadvisor.Perfil', through='tripadvisor.Avaliacao') # conexão com Avalia.
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome