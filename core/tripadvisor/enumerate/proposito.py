from django.db import models

class Proposito(models.TextChoices):
    BUSINESS = "Negócios"
    VACATION = "Férias"
    BACKPACKING = "Mochilão"
    ACADEMIC = "Academico"
    OUTRO = "Outro"
