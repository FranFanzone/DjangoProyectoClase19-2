from django.urls import path
from App1.views import *

urlpatterns = [
    path('',inicio),
    path('Agregar_Profe/',agregarProfe),
    path('Estudiantes/',estudiantes),
    path('Profesores/',profesores),
    path('Entregables/',entregables),
    path('Cursos/',cursos),
]