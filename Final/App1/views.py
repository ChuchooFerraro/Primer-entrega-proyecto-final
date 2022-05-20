from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from datetime import datetime


# Create your views here.

def fechaa(request):
    dia= datetime.now()
    texto = f"Hoy es: <br>{dia}"
    return HttpResponse(texto)

def azul(request):
    return render(request, "App1/azul.html")

def start_boostrap(request):
    return render(request, "App1/index.html")
