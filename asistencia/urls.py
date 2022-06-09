from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('seccion1',views.seccion1, name='seccion1')
]
