from .base_manager import BaseManager
from django.forms.models import model_to_dict

class QuestaoManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"


    # Questões abertas == "Não Respondida"
    def find_abertas(self, s:str = "estacionamento") -> set["Questao"]:
        consulta = self.filter(status__contains="Não Respondida", texto__contains=s)
        return set(consulta)

