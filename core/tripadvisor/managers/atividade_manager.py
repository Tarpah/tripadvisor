from django.db.models import QuerySet
from django.forms.models import model_to_dict
from .base_manager import BaseManager
class AtividadeManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    def find_by_dificuldade_idioma(self, dificuldade, pais:str) -> QuerySet['Atividade']:
        consulta = self.filter(dificuldade__contains=dificuldade, endereco__pais__contains=pais)
        return consulta


    def find_by_preco(self,valor_1:float = 100, valor_2:float = 300) -> QuerySet['Atividade']:
        consulta = self.filter(valor__gt=valor_1, valor__lt=valor_2)
        return consulta


    def find_by_categoria_duracao(self) -> set['Atividade']:
        # coloquei Turnê no banco pela restrição da categoria ser 5 caracteres sendo "tour" não registrável
        consulta = self.filter(categorias__nome__icontains="Turn", duracao__gt="03:00")
        return set(consulta)

    # Troque "RS" por "Rio Grande do Sul", o banco está com restrição para não aceitar string com menos de 5 caracteres.
    def find_atividades_estado_preco(self, e: str = "Rio Grande do Sul", pi: float = 100.0, pf: float = 500.0):
        consulta = self.filter(endereco__estado__icontains=e, valor__gte=pi, valor__lte=pf)
        return consulta


    def find_by_participantes_e_nota(self) -> QuerySet['Atividade']:
        consulta_1 = self.filter(participantes__gt=10)
        consulta_2 = self.filter(nota__gte=4)

        consulta = consulta_1.union(consulta_2)
        return consulta


    def ranking(self) -> tuple['Atividade']:
        consulta = self.filter().order_by("-nota")

        return tuple(consulta)


