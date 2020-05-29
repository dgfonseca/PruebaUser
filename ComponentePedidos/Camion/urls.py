from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^camiones/', views.camiones_list),
    url(r'^camioncreate/$', csrf_exempt(views.camion_create), name='camioncreate'),
]
