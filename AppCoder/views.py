from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.

def crea_curso(self, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)

    curso.save()

    return HTTPResponse(f'Se creo el curso de {curso.nombre} con el numero de camada {curso.camada}')

