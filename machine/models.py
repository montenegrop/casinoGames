from django.db import models

# Create your models here.


class machine(models.Model):
    # identificar la maquina que estamos usando
    configuration = models.CharField(max_length=10000, default="")
    # corregir:
    # ver si se puede mejorar
