from django.db import models

class Turno(models.TextChoices):
    MORNING = "Manhã"
    AFTERNOON = "Tarde"
    NIGHT = "Noite"
    EARLY_MORNING = "Madrugada"