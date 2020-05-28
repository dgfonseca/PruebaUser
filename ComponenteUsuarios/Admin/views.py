from django.shortcuts import render
import os, hashlib
from .models import Administrador
from django.http import JsonResponse, HttpResponse
import json


def administradores_list(request):
    queryset = Administrador.objects.all()
    context = list(queryset.values('nombre', 'cedula', 'telefono', 'contrasena', 'bitacora'))
    return JsonResponse(context, safe=False)

def administrador_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        admin = Administrador()
        admin.nombre = data_json['nombre']
        admin.cedula = data_json['cedula']
        admin.telefono = data_json['telefono']
        admin.contrasena = hash_password(data_json['contrasena'])
        admin.bitacora = ['bitacora']
        admin.save()
        return HttpResponse("Creado correctamente")
    else:
        return HttpResponse("No se creó, problemas")

def hash_password(contrasena):
    password = str(contrasena)
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    return hash

