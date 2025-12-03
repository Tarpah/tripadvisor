from django.db.models import QuerySet

from .base_manager import BaseManager
from django.forms.models import model_to_dict

class ViagemManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_futuras_by_destino(self, d: str = "Brasil") -> QuerySet['Viagem']:
        consulta = self.filter(pais_destino__contains=d)
        return consulta


    def find_by_orcamento(self, o: float = 10000.0)-> list['Viagem']:
        consulta = self.filter(orcamento__gt=o)
        return list(consulta)


    def find_viagens_pelo_brasil(self)-> set['Viagens']:
        consulta = self.filter(atracao__endereco__pais__contains="Brasil")
        return set(consulta)


    def find_viagens_dificeis(self) -> set['Viagem']:
        consulta = self.filter(atracao__atividade__dificuldade="Difícil")
        return set(consulta)
