from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from App1.models import *

def inicio(request):
    
    return render(request, 'App1/Inicio.html')
    

def agregarProfe(request):

    profe1 = Profesor(nombre='Profe',apellido='Coder',edad=38,email='profe@coder.com')
    profe1.save()

    return HttpResponse(f'Se agrego el profesor {profe1.nombre} {profe1.apellido}.')

def estudiantes(request):
    return render(request, 'App1/verEstudiante.html')

def profesores(request):
    
    return render(request, 'App1/verProfesores.html')

def entregables(request):
    return render(request, 'App1/verEntregables.html')

def cursos(request):
    return render(request, 'App1/verCursos.html')