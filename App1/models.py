from django.db import models

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.CharField(max_length=40)
    email = models.EmailField()

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    entregado = models.BooleanField()

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField()



