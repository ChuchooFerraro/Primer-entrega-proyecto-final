from django.db import models

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=20)
    camada = models.IntegerField()

class Alumno(models.Model):
    name = models.CharField()
    born = models.DateField()
    email = models.EmailField()

class Profesor(models.Model):
    name = models.CharField()
    born = models.DateField()
    email = models.EmailField()