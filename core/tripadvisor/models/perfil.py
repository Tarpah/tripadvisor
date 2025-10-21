from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from tripadvisor.enumerate import Genero
from tripadvisor.validators import verifica_maior_idade

class Perfil(BaseModel):
    email = models.CharField(validators=[MinLengthValidator(10)], max_length=100)
    nome = models.CharField(validators=[MinLengthValidator(10)], max_length=100)
    passaporte = models.CharField(validators=[MinLengthValidator(10)], max_length=10)
    senha = models.CharField(validators=[MinLengthValidator(5)], max_length=20)
    data_nascimento = models.DateField(validators=[verifica_maior_idade]) # verificador não ficou bom refazer depois
    pais = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    genero = models.CharField(max_length=13, choices=Genero, default=Genero.NOT_INFORMED)
    pagina_pessoal = models.URLField(validators=[MinLengthValidator(15)], max_length=150, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    lingua = models.CharField(validators=[MinLengthValidator(5)], max_length=20, null=True, blank=True)
    premium = models.BooleanField(default=False)
    membro_desde = models.DateField(auto_now_add=True) # é automático? perguntar ao professor.


    def __str__(self):
        return self.nome