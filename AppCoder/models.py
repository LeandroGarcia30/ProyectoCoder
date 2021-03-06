import email
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField('nombre', max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField('nombre', max_length=40)
    apellido = models.CharField('apellido', max_length=40)
    fecha_inscripcion = models.DateField('fehca', auto_now_add=False)

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado= models.BooleanField()
