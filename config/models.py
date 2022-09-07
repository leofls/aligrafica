from django.db import models
from colorfield.fields import ColorField

class Config(models.Model):
    info = models.CharField(max_length=250, verbose_name="Info config", default="Info config")
    icon = models.CharField(max_length=150, null=True, blank=True)
    color = ColorField(default='#FF0000')
    contact = models.JSONField(verbose_name="Dados contato", null=True, blank=True)

    def __str__(self):
        return self.info
