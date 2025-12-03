from .base_manager import BaseManager
from django.forms.models import model_to_dict
class AtracaoManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return print(dados)

        except self.model.DoesNotExist:
            return "Não encontrado"


    def ranking(self) -> tuple['Atracao']:
        consulta = self.filter().order_by("-nota")
        return tuple(consulta)



