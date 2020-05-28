from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^tiendas/', views.tiendas_list),
    url(r'^tiendacreate/$', csrf_exempt(views.tienda_create), name='tiendacreate'),
]