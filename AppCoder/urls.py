from django.urls import path
from .views import *


urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('inicio/', inicio, name="inicio"),
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('profeFormulario/', profeFormulario, name="profeFormulario"),
    path('busquedaComision/', busquedaComision, name="busquedaComision"),
    path('buscar/', buscar, name="buscar"),
    path('leerProfesores/', leerProfesores, name="leerProfesores"),
    path('eliminarProfesor/<id>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<id>', editarProfesor, name="editarProfesor"),
    path('leerPersonas/', leerPersonas, name="leerPersonas"),
    path('agregarPersona/', agregarPersona, name="agregarPersona"),
]