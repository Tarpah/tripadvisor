from django.contrib import admin
from .models import Atividade, Local, Categoria, Perfil, Atracao, Avaliacao, Questao, Resposta, Viagem, Endereco

admin.site.register((Atividade, Local, Categoria, Perfil, Atracao, Avaliacao, Questao, Resposta, Viagem, Endereco))