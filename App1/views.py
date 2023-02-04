from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from App1.models import *


def mostrarPagina(request):
    
    diccionario = {}
    
    miHtml = open('C:/Users/franc/OneDrive/Escritorio/Python/DjangoCursoPractica/DjangoProyectoClase19-2/Proyecto2/plantillas/plantilla1.html')

    plantilla = Template(miHtml.read())
    
    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def agregarProfe(request):

    profe1 = Profesor(nombre='Profe',apellido='Coder',edad=38,email='profe@coder.com')
    profe1.save()

    return HttpResponse(f'Se agrego el profesor {profe1.nombre} {profe1.apellido}.')