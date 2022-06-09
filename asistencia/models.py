from distutils.command.upload import upload
from pydoc import describe
from django.db import models

# Create your models here.
class Estudiante(models.Model):
  id = models.AutoField(primary_key=True)
  nombres = models.CharField(max_length=100, verbose_name='nombres')
  apellidos = models.CharField(max_length=100, verbose_name='apellidos')
  imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
  descripcion = models.TextField(verbose_name='Descripcion', null=True)
