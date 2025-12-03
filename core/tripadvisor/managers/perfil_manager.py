from django.db.models import Count, QuerySet
from django.forms.models import model_to_dict
from .base_manager import BaseManager
from datetime import datetime

class PerfilManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_novos_ultimo_mes(self) -> QuerySet["Perfil"]:
        mes_atual = datetime.now().month
        ano_atual = datetime.now().year

        # janeiro
        if mes_atual == 1:
            consulta = self.filter(membro_desde__gte=f'{ano_atual-1}-{12}-01')
            return consulta

        # resto do ano
        consulta = self.filter(membro_desde__gte=f'{ano_atual}-{mes_atual-1}-01')
        return consulta


    def find_perfis_educacionais(self) -> QuerySet["Perfil"]:
        consulta = self.filter(email__contains="edu")
        return consulta


    def find_by_idioma_questoes_respondidas(self, i:str = "Português", q: int = 2) -> QuerySet['Perfil']:
        consulta = self.filter(
            lingua=i,
            questao__status__exact="Respondida").annotate(
            qnt_respondidas=Count('questao')).filter(
                qnt_respondidas__gte=q)

        return consulta


    def find_by_avaliacao_museu(self) -> QuerySet['Perfil']:
        consulta = self.filter(avaliacao__atracao__categorias__nome__icontains="museu")

        return consulta