from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class JugadaTest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='jugadas')
    played_date = models.DateField(default=timezone.now)
    # roll = models.JSONField()
    roll_string = models.CharField(max_length=100)
    bet = models.FloatField(verbose_name="bet", default=0)

    # corregir:
    # agregar identificador de configuracion de maquina
