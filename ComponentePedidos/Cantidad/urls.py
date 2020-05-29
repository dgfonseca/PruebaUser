from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^cantidades/', views.cantidades_list),
    url(r'^cantidadcreate/$', csrf_exempt(views.cantidad_create), name='cantidadcreate'),
]
