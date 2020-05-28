from django.db import models

class TiendaDeBarrio(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.FloatField(null=True, blank=True, default=None)
    contrasena = models.CharField(max_length=100)
    nit = models.FloatField(unique=True, null=True, blank=True, default=None, editable=False)
    direccion = models.CharField(max_length=500)



