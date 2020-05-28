from django.db import models

class Camion(models.Model):
    placa = models.CharField(max_length=6, primary_key=True)
    SOAT = models.IntegerField(default=None, blank=True, null=False)
    noRevisionTM = models.IntegerField(default=None, blank=True, null=False)
    camionero = models.IntegerField(null=False, default=None)
