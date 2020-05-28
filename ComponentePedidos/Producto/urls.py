from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^productos/', views.productos_list),
    url(r'^productocreate/$', csrf_exempt(views.producto_create), name='productocreate'),
]