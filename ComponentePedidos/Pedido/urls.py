from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^pedidos/', views.pedidos_list),
    url(r'^pedidocreate/$', csrf_exempt(views.pedido_create), name='pedidocreate'),
]