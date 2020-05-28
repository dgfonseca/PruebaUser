from django.shortcuts import render
import os, hashlib
from .models import Camionero
from django.http import JsonResponse, HttpResponse
import json


def camioneros_list(request):
    queryser = Camionero.objects.all()
    context = list(queryser.values('nombre', 'cedula', 'telefono', 'contrasena','numeroRunt','sueldo'))
    return JsonResponse(context, safe=False)

def camionero_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        camionero = Camionero()
        camionero.nombre = data_json['nombre']
        camionero.cedula = data_json['cedula']
        camionero.telefono = data_json['telefono']
        camionero.contrasena = hash_password(data_json['contrasena'])
        camionero.bitacora = ['numeroRunt']
        camionero.sueldo = ['sueldo']
        camionero.save()
        return HttpResponse("Creado correctamente")
    else:
        return HttpResponse("No se creó, problemas")

def hash_password(contrasena):
    password = str(contrasena)
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    return hash
