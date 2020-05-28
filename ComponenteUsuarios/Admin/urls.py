from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^admins/', views.administradores_list),
    url(r'^admincreate/$', csrf_exempt(views.administrador_create), name='admincreate'),
]