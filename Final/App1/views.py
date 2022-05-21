from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from datetime import datetime
from App1.models import Curso
from App1.forms import Cursoformulario

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