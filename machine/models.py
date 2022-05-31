from re import T
from django.db import models

from machine.computations.examples import victorious_payment
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Machine(models.Model):

    def empty_list():
        return list()
    # identificar la maquina que estamos usando
    name = models.CharField(max_length=200, blank=True)

    payments = models.JSONField()
    free_spins = ArrayField(models.IntegerField(blank=True),
                            size=5, default=empty_list)

    roi = models.FloatField(default=0)

    normal_reel = ArrayField(
        models.CharField(max_length=200, blank=True),
        size=5, default=empty_list
    )
    bonus_reel = ArrayField(
        models.CharField(max_length=200, blank=True),
        size=5, default=empty_list
    )
    visible = ArrayField(
        models.IntegerField(blank=True),
        size=5, default=empty_list
    )

    # corregir:
    # ver si se puede mejorar

    def payment(self, roll):
        return victorious_payment(self, roll)

    def save(self, *args, **kwargs):
        self.roi += 0.01
        super(Machine, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
