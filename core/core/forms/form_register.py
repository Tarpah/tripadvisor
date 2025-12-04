from .base_form import BaseForm
from django.contrib.auth.models import User

class RegisterForm(BaseForm):
    class Meta:
        model = User
        fields = ['username', 'password']