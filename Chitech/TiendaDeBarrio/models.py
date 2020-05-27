from django.db import models
import os
import hashlib


# Create your models here.

class TiendaDeBarrio(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.FloatField(primary_key=True, default=None, blank=True)
    telefono = models.FloatField(null=True, blank=True, default=None)
    contrasena = models.CharField(max_length=100)
    nit = models.FloatField(unique=True, null=True, blank=True, default=None, editable=False)
    direccion = models.CharField(max_length=500)
    ventasMensuales = models.FloatField(null=True, blank=True, default=None)
    hashed = models.BooleanField(default=False, editable=False)

    def update_hash2(self):
        if not self.hashed:
            self.contrasena=hash_password(self.contrasena)
            self.hashed=True
            self.save(force_update=True)
        return hash_password(self.contrasena)


def hash_password(contrasena):
    password = str(contrasena)
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    return hash
