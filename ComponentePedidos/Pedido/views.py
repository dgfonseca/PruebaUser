from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
from .models import Pedido
import json


def check_tienda(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept": "application/json"})
    tiendas = r.json()
    for tienda in tiendas:
        if data["tienda"] == tienda["nit"]:
            return True
    return False


def pedidos_list(request):
    queryset = Pedido.objects.all()
    context = list(queryset.values('id', 'fechaSolicitud', 'fechaEntrega', 'camion', 'factura', 'tienda'))
    return JsonResponse(context, safe=False)


def pedido_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_tienda(data_json) == True:
            pedido = Pedido()
            pedido.fechaSolicitud = data_json['fechaSolicitud']
            pedido.fechaEntrega = data_json['fechaEntrega']
            pedido.tienda = data_json['tienda']
            pedido.factura = data_json['factura']
            pedido.camion = ['camion']
            pedido.save()
            return HttpResponse("Creado correctamente")
        else:
            return HttpResponse("No se creó, problemas")
