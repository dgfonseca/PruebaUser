from django.db import models
import os,hashlib

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.FloatField(primary_key=True, default=None, blank=True)
    telefono = models.FloatField(null=True, blank=True, default=None)
    contrasena = models.CharField(max_length=100)
    bitacora = models.CharField(max_length=500)

