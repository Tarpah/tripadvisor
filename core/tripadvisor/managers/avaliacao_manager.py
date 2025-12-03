from django.db.models import QuerySet
from .base_manager import BaseManager
from datetime import datetime
from django.forms.models import model_to_dict


class AvaliacaoManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return print(dados)

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_avaliacoes_atuais(self) -> list['Avaliacao']:
        ano_atual = datetime.today().year
        consulta = self.filter(data_avaliacao__gte=f'{ano_atual}-01-01')
        return list(consulta)


    def find_melhores_portugues(self, lingua="Português") -> QuerySet['Avaliacao']:
        consulta = self.filter(perfil__lingua=lingua, nota=5)
        return consulta


    def find_uteis_by_local(self, local) -> QuerySet['Avaliacao']:
        consulta = self.filter(atracao__local__nome__icontains=local, atracao__local__nota=10)
        return consulta


    def find_by_titulo_nota(self, t:str = "Ótimo", n:int = 7):
        consulta = self.filter(texto__startswith=t, nota__gte=n)
        return consulta




