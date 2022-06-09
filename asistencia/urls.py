from unicodedata import name
from django.urls import path
from numpy import safe_eval
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('seccion1',views.seccion1, name='seccion1'),
    path('asistencia',views.asistencia, name='asistencia')
]
