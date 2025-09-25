from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now=True) # apenas para registro
    update_at = models.DateTimeField(auto_now=True) # apenas para registro

    class Meta:
        abstract = True # não cria objetos
        app_label = 'tripadvisor'