from django.core.validators import ValidationError
from datetime import date

def verifica_maior_idade(data_registrada):
    today = date.today()
    tempo_delta = today - data_registrada

    if tempo_delta.days < 6570: # 6570 são 18 anos em dias, não contabiliza ano bissexto
        raise ValidationError(f'Perfil deve ser maior de idade!')