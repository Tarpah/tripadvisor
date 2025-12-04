from .base_form import BaseForm
from tripadvisor.models import Atracao

class AtracaoForm(BaseForm):
    class Meta:
        model = Atracao
        fields = '__all__'