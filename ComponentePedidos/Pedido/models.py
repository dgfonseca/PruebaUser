from django.db import models
from Camion.models import Camion
class Pedido(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
    fechaSolicitud = models.CharField(max_length=6, default=None)
    fechaEntrega = models.CharField(max_length=6, default=None)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, null=True)
    tienda = models.IntegerField(null=False, default=None)
