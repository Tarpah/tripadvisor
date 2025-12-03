from django.db.models import QuerySet

from .base_manager import BaseManager
from django.forms.models import model_to_dict

class RespostaManager(BaseManager):
    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_by_idioma(self, i:str="Português") -> QuerySet['Resposta']:
        consulta = self.filter(perfil__lingua__contains="Português")
        return consulta


    def find_by_palavras(self) -> QuerySet['Resposta']:
        consulta_titulo_1 = self.filter(titulo__contains="impróprio")
        consulta_titulo_2 = self.filter(titulo__contains="decepção")
        consulta_titulo_3 = self.filter(titulo__contains="ilusão")

        consulta_texto_1 = self.filter(texto__contains="impróprio")
        consulta_texto_2 = self.filter(texto__contains="decepção")
        consulta_texto_3 = self.filter(texto__contains="ilusão")

        consulta = (
                consulta_titulo_1 | consulta_titulo_2 | consulta_titulo_3 |
                consulta_texto_1 | consulta_texto_2 | consulta_texto_3
        ).distinct()

        return consulta