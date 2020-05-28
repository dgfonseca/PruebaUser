from django.db import models
from Pedido.models import Pedido
from Producto.models import ProductosTienda

class Cantidad(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
    numeroProductos = models.FloatField(max_length=100)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='cantidades', null=False)
    producto = models.ForeignKey(ProductosTienda,on_delete=models.CASCADE, related_name='cantidades', null=False)
