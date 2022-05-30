"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App1 import views



urlpatterns = [
    path('', views.start_boostrap, name='Home'),
    path('profesores/', views.profesores, name ='Profesores'),
    path('cursos/', views.cursos, name ='Cursos'),
    path('alumnos/', views.alumnos, name ='Alumnos'),
    
    #Forms
    path('profesores_form/', views.profesor_forms_django, name ='Profesores_form'),
    path('alumnos_form/', views.alumno_forms_django, name ='Alumnos_form'),
    path('cursos_form/', views.curso_forms_django, name ='Cursos_form'),
    
    #Busqueda
    path('cursos_search/', views.cursos_search, name ='cursos_search'),
]
