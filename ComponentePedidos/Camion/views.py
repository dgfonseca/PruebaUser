from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
from .models import Camion
import json

def check_camionero(data):
    r = requests.get(settings.PATH_VAR2, headers={"Accept": "application/json"})
    camioneros = r.json()
    for camionero in camioneros:
        if data["camionero"] == camionero["cedula"]:
            return True
    return

def camiones_list(request):
    queryset = Camion.objects.all()
    context = list(queryset.values('placa', 'SOAT', 'noRevisionTM', 'camionero'))
    return JsonResponse(context, safe=False)


def camion_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_camionero(data_json) == True:
            camion = Camion()
            camion.placa = data_json['placa']
            camion.SOAT = data_json['SOAT']
            camion.noRevisionTM = data_json['noRevisionTM']
            camion.camionero = data_json['camionero']
            camion.save()
            return HttpResponse("Creado correctamente")
        else:
            return HttpResponse("No se creó, problemas")
