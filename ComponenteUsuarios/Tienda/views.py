from django.shortcuts import render
import os, hashlib
from .models import TiendaDeBarrio
from django.http import JsonResponse, HttpResponse
import json


def tiendas_list(request):
    queryser = TiendaDeBarrio.objects.all()
    context = list(queryser.values('nombre', 'telefono', 'contrasena', 'nit', 'direccion'))
    return JsonResponse(context, safe=False)


def tienda_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        tienda = TiendaDeBarrio()
        tienda.nombre = data_json['nombre']
        tienda.telefono = data_json['telefono']
        tienda.contrasena = hash_password(data_json['contrasena'])
        tienda.nit = ['nit']
        tienda.direccion = ['direccion']
        tienda.save()
        return HttpResponse("Creado correctamente")
    else:
        return HttpResponse("No se creó, problemas")


def hash_password(contrasena):
    password = str(contrasena)
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    return hash
