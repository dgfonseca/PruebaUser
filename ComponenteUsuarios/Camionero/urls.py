from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^camioneros/', views.camioneros_list),
    url(r'^camionerocreate/$', csrf_exempt(views.camionero_create), name='camionerocreate'),
]