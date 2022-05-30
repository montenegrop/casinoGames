from re import T
from django.db import models

from machine.computations.examples import victorious_payment
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Machine(models.Model):
    # identificar la maquina que estamos usando
    configuration = models.CharField(max_length=10000, default="")
    reels_round = ArrayField(
        models.CharField(max_length=200, blank=True),
        size=5,
    )
    payments = models.JSONField()
    free_spins = ArrayField(models.IntegerField(blank=True),
                            size=5)

    roi = models.FloatField(default=0)

    # corregir:
    # ver si se puede mejorar

    def payment(self, roll):
        return victorious_payment(self, roll)

    def save(self, *args, **kwargs):
        self.roi += 0.01
        super(Machine, self).save(*args, **kwargs)
