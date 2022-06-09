from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request): #definimos la vista inicio
  return HttpResponse("<h1>Bienvenido al Inicio</h1>")

def seccion1(request):
  return render(request, 'paginas/seccion1.html') #renderizamos el archivo seccion1.html

