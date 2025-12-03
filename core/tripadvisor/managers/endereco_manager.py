from .base_manager import BaseManager
from django.forms.models import model_to_dict

class EnderecoManager(BaseManager):

    def find_by_id(self, pk_pesquisado):
        try:
            consulta = self.get(pk=pk_pesquisado)

            dados = model_to_dict(consulta)
            return dados

        except self.model.DoesNotExist:
            return "Não encontrado"

    def find_by_cep(self) -> list['Endereco']:
        enderecos = self.filter(cep__contains='90')

        ids = []
        for encereco in enderecos:
            if encereco.cep[:2] == '90':
               ids.append(encereco.pk)

        consulta = self.filter(pk__in=ids)
        # depois de fazer a solução acima descobri que dava pra fazer: consulta = self.filter(cep__startswith='90')

        return list(consulta)



