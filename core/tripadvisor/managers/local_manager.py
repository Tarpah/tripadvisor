from django.db.models import QuerySet, Count
from django.forms.models import model_to_dict

from .base_manager import BaseManager
from datetime import datetime

class LocalManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_by_cidade(self, cidade:str) -> QuerySet['Local']:
        consulta = self.filter(endereco__cidade__icontains=cidade)
        return consulta


    def find_by_nota_minima(self, nota) -> QuerySet['Local']:
        consulta = self.filter(nota__gte=nota)
        return consulta


    def find_by_local_pais(self, pais_pesquisado) -> QuerySet['Local']:
        consulta = self.filter(endereco__pais__exact=pais_pesquisado)
        return consulta


    def find_by_no_endereco(self) -> list['Local']:
        consulta = self.filter(endereco__isnull=False)
        return list(consulta)


    def find_by_site_br(self)-> list['Local']:
        consulta = self.filter(site__icontains='.br')
        return list(consulta)


    def find_romantico_or_familia(self)-> list['Local']:
        consulta_temp_1 = self.filter(categorias__nome__icontains="romântico")
        consulta_temp_2 = self.filter(categorias__nome__icontains="família")
        consulta = (consulta_temp_1 | consulta_temp_2).distinct()
        # achei legal essa de cima o mais normal é consulta = consulta_temp_1.union(consulta_temp_2)

        return list(consulta)


    def find_avaliados_by_novos_usuarios(self, ano:int = 2025) -> QuerySet['Local']:
        consulta = self.filter(avaliacao__perfil__membro_desde__year=ano)
        return consulta


    #  Locais com pelo menos 50 avaliações
    def find_by_numero_avaliacoes(self, numero:int = 50)-> QuerySet['Local']:
        consulta = self.annotate(
            total_avaliacoes=Count('avaliacao')
        ).filter(
            total_avaliacoes__gte=numero
        )
        return consulta


    def find_visitados_avaliados_by_perfil(self) -> list['Local']:
        hoje = datetime.today()
        consulta = self.filter(viagens__final__lte=hoje, avaliacoes__isnull=False).order_by('nome').distinct()
        return list(consulta)


    def find_visitados_ultimo_ano(self) -> list['Local']:
        ultimo_ano = datetime.today().year - 1

        consulta_temp_1 = self.filter(avaliacao__perfil__viagem__inicio__year=ultimo_ano)
        consulta_temp_2 = self.filter(avaliacao__perfil__viagem__final__year=ultimo_ano)

        consulta = consulta_temp_1.union(consulta_temp_2)
        return list(consulta)


    def find_locais_avaliados_by_datas(self,data_inicial:datetime, data_final:datetime) -> QuerySet['Local']:
        consulta = self.filter(avaliacao__data_avaliacao__gte=data_inicial, avaliacao__data_avaliacao__lte=data_final)
        return consulta


    def find_contato_parcial(self) -> QuerySet['Local']:
        consulta = self.filter(site__isnull=False, telefone__isnull=True)
        return consulta


    def find_by_avaliacao_premium(self) -> tuple['Local']:
        consulta = self.filter(avaliacao__data_avaliacao__year=2025, avaliacao__perfil__premium=True)
        return tuple(consulta)


    def ranking(self) -> tuple['Local']:
        consulta = self.filter().order_by("-nota")

        return tuple(consulta)