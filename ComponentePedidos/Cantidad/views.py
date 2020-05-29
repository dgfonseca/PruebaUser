from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
from .models import Cantidad
from Producto.models import ProductosTienda
from Pedido.models import Pedido
import json




def cantidades_list(request):
    queryset = Cantidad.objects.all()
    context = list(queryset.values('id', 'numeroProductos', 'pedido', 'producto'))
    return JsonResponse(context, safe=False)


def cantidad_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cantidad = Cantidad()
        cantidad.numeroProductos = data_json['numeroProductos']
        pk_pedido = data_json['pedido']
        queryset = Pedido.objects.filter(id=pk_pedido)
        context = list(queryset.values('id', 'fechaSolicitud', 'fechaEntrega', 'tienda'))
        print(context)
        pedido = Pedido()
        pedido.id = context[0]['id']
        pedido.fechaEntrega = context[0]['fechaEntrega']
        pedido.fechaSolicitud = context[0]['fechaSolicitud']
        pedido.tienda = context[0]['tienda']
        cantidad.pedido = pedido
        pk_producto = data_json['producto']
        queryset2 = ProductosTienda.objects.filter(EAN = pk_producto)
        context2 = list(queryset2.values('nombre', 'EAN', 'precio', 'tipo'))
        producto = ProductosTienda()
        producto.nombre =context2[0]['nombre']
        producto.EAN = context2[0]['EAN']
        producto.precio = context2[0]['precio']
        producto.tipo = context2[0]['tipo']
        cantidad.producto = producto
        cantidad.save()
        return HttpResponse("Creado correctamente")
    else:
        return HttpResponse("No se creó, problemas")
