from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def curso(request):
    cursito=Curso(nombre="JavaScript", comision=123456)
    cursito.save()
    cadena_texto=f"curso guardado: Nombre {cursito.nombre}, Comision: {cursito.comision}"
    return HttpResponse(cadena_texto)