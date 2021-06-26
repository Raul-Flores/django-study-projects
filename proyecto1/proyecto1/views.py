from django.http import HttpResponse
import datetime
from django.shortcuts import render

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #Primera vista
    p1 = Persona("Raul", "Flores")
    return render(request, 'miplantilla.html', {'nombre_persona':p1.nombre, 'apellido_persona':p1.apellido})

def cursopyton(request):
    hoy = datetime.datetime.now()
    return render (request, "cursopython.html", {"damefecha": hoy})

def clasegit(request):
    hoy = datetime.datetime.now()
    return render (request, "clasegit.html", {"damefecha": hoy})