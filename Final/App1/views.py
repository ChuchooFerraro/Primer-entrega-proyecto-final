from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from datetime import datetime
from App1.models import Curso
from App1.models import Profesor
from App1.models import Alumno
from App1.forms import Profesor_form, Alumno_form, Curso_form

# Create your views here.

def start_boostrap(request):
    return render(request, "App1/index.html")


def profesores(request):
    profesors = Profesor.objects.all()

    context_dict = {
        'profesors': profesors
    }
    return render(request, 'App1/profesores.html',context_dict)

def cursos(request):
    cursos = Curso.objects.all()
    
    context_dict = {
        'cursos': cursos
    }
    return render(request, 'App1/cursos.html',context_dict)

def alumnos(request):
    alumnos = Alumno.objects.all()
    
    context_dict = {
        'alumnos': alumnos
    }
    return render(request, 'App1/alumnos.html',context_dict)

#-----------------------------FORMULARIOS-----------------------------------------------------------------

def profesor_forms_django(request):
    if request.method == 'POST':

        profesor_form = Profesor_form(request.POST)
        

        if profesor_form.is_valid():
            data = profesor_form.cleaned_data

            profesor = Profesor(
                name=data["name"],
                born=data['born'],
                email=data['email'],
            )
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="App1/profesores.html"
            )

    profesor_form = Profesor_form(request.POST)
    context_dict = {
        'profesor_form': profesor_form
    }
    return render(
    request=request,
    context=context_dict,
    template_name='App1/profesores_form.html'
    )

def alumno_forms_django(request):
    if request.method == 'POST':

        alumno_form = Alumno_form(request.POST)
        

        if alumno_form.is_valid():
            data = alumno_form.cleaned_data

            alumno = Alumno(
                name=data["name"],
                born=data['born'],
                email=data['email'],
            )
            alumno.save()

            alumnos = Alumno.objects.all()
            context_dict = {
                'alumnos': alumnos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="App1/alumnos.html"
            )

    alumno_form = Alumno_form(request.POST)
    context_dict = {
        'alumno_form': alumno_form
    }
    return render(
    request=request,
    context=context_dict,
    template_name='App1/alumnos_form.html'
    )

def curso_forms_django(request):
    if request.method == 'POST':

        curso_form = Curso_form(request.POST)
        

        if curso_form.is_valid():
            data = curso_form.cleaned_data

            curso = Curso(
                curso=data["curso"],
                camada=data['camada'],
            )
            curso.save()

            cursos = Curso.objects.all()
            context_dict = {
                'cursos': cursos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="App1/cursos.html"
            )

    curso_form = Curso_form(request.POST)
    context_dict = {
        'curso_form': curso_form
    }
    return render(
    request=request,
    context=context_dict,
    template_name='App1/cursos_form.html'
    )

    #-------------------------------------BUSQUEDAS------------------------------------------------------------