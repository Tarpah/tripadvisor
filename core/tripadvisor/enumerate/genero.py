from django.db import models

class Genero(models.TextChoices):
    MAN = "Homem"
    WOMAN = "Mulher"
    NON_BINARY = "Não Binário"
    NOT_INFORMED = "Não Informado"

