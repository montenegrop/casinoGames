from django.db import models

from machine.computations import victorious_payment

# Create your models here.


class machine(models.Model):
    # identificar la maquina que estamos usando
    configuration = models.CharField(max_length=10000, default="")
    # corregir:
    # ver si se puede mejorar

    def payment(self, roll):
        return victorious_payment(self, roll)
