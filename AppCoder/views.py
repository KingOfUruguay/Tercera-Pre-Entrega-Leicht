from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarollo Web', camada='19881')
    curso.save()

    documentodetexto = f'---->Curso: {curso.nombre} Camdada: {curso.camada}'

    return HttpResponse(documentodetexto)
