from django.db import models

class ProductosTienda(models.Model):
    nombre = models.CharField(max_length=100)
    EAN = models.FloatField(primary_key=True, default=None, blank=True)
    precio = models.FloatField(max_length=100, default=None)
    tipo = models.CharField(max_length=100)
