from django.shortcuts import render
import os, hashlib
from .models import ProductosTienda
from django.http import JsonResponse, HttpResponse
import json


def productos_list(request):
    queryser = ProductosTienda.objects.all()
    context = list(queryser.values('nombre', 'EAN', 'precio', 'tipo'))
    return JsonResponse(context, safe=False)

def producto_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        camionero = ProductosTienda()
        camionero.nombre = data_json['nombre']
        camionero.EAN = data_json['EAN']
        camionero.precio = data_json['precio']
        camionero.tipo = data_json['tipo']
        camionero.save()
        return HttpResponse("Creado correctamente")
    else:
        return HttpResponse("No se creó, problemas")
