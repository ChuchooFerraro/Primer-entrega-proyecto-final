from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from datetime import datetime
from App1.models import Curso
from App1.forms import Cursoformulario
from App1.models import Profesor
from App1.models import Alumno
from App1.forms import Profesor_form

# Create your views here.

def fechaa(request):
    dia= datetime.now()
    texto = f"Hoy es: <br>{dia}"
    return HttpResponse(texto)

def azul(request):
    return render(request, "App1/azul.html")

def start_boostrap(request):
    return render(request, "App1/index.html")

def formulario(request):

    if request.method == 'POST':
        miform = Cursoformulario(request.POST)
        print(miform)

        if miform.is_valid:
            info = miform.cleaned_data
            curso = Curso (curso = info['curso'], camada = info['camada'])
            curso.save()
            return render(request,'App1/formulario.html')
    else:
        miform = Cursoformulario()
        return render(request,'App1/formulario.html',{"miform":miform})

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

def profesor_forms_django(request):
    if request.method == 'POST':
        profesor_form = Profesor_form(request.POST)

        if profesor_form.is_valid():
            data = profesor_form.cleaned_data

            profesor = Profesor(
                name=data['Nombre'],
                #born=data['Nacimiento'],
                email=data['Email'],
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