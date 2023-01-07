from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Curso, Profesor, Persona
from AppCoder.forms import CursoForm, ProfeForm, PersonaForm, RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def curso(request):

    curso1=Curso(nombre="SQL", comision=5478)
    curso1.save()
    curso2=Curso(nombre="Django", comision=8142)
    curso2.save()

    lista_cursos=[curso1, curso2]
    
    cadena_texto=f"curso guardado: Nombre {curso1.nombre}, Comision: {curso1.comision}"
    return render(request,"AppCoder/curso.html", {"cursos":lista_cursos})
    return HttpResponse(cadena_texto)

def cursos(request):
    return render(request, "Appcoder/cursos.html")




def profesores(request):
    return render(request, "Appcoder/profesores.html")

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")

def inicio(request):
    return render(request, "Appcoder/inicio.html")

'''
def cursoFormulario(request): #Nos permite crear un curso por formulario
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request, "AppCoder/inicio.html", {"mensaje": "Curso guardado correctamente"})
    else:
        return render(request, "AppCoder/cursoFormulario.html")'''


def cursoFormulario(request):
    if request.method=="POST":
        form= CursoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Curso guardado correctamente"})
        else:
            return render(request, "AppCoder/cursoFormulario.html", {"form":form, "mensaje": "Info no valida"})

    else:
        formulario=CursoForm()
        return render(request, "AppCoder/cursoFormulario.html", {"form":formulario})


def profeFormulario(request):
    if request.method=="POST":
        form= ProfeForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            profesion=informacion["profesion"]
            curso= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            curso.save()
            profesores=Profesor.objects.all()
            return render(request, "AppCoder/profesores.html", {"profesores":profesores,"mensaje": "Profe guardado correctamente"})
        else:
            return render(request, "AppCoder/profeFormulario.html", {"form":form, "mensaje": "Info no valida"})

    else:
        formulario=ProfeForm()
        return render(request, "AppCoder/profeFormulario.html", {"form":formulario})


def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):

    comision=request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision=comision)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Ingres una comision para buscar!"})


def leerProfesores(request):
    profesores=Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"mensaje":"LISTADO COMPLETO:","profesores": profesores})


def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)  #Cuando llamo al profe, me lo trae, para luego eliminar.
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "AppCoder/Profesores.html", {"profesor":profesores,"mensaje":"Profesor eliminado correctamente"})


def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id) #Traje al profe que quiero editar
    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, "AppCoder/Profesores.html", {"mensaje": "Profesor editado correctamente"})

    else:
        formulario= ProfeForm(initial={"nombre":profesor.nombre,"apellido":profesor.apellido,"email":profesor.email,"profesion":profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html",{"form":formulario,"profesor":profesor} )  
    
def leerPersonas(request):
    personas= Persona.objects.all()
    return render(request, "AppCoder/personas.html", {"personas":personas})


def agregarPersona(request):
    if request.method=="POST":
        formulario=PersonaForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            dni=info["dni"]
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            fecha_nacimiento=info["fechaNacimiento"]
            tieneObraSocial=info["tieneObraSocial"]
            persona= Persona(dni=dni,nombre=nombre,apellido=apellido,email=email,fechaNacimiento=fecha_nacimiento,tieneObraSocial=tieneObraSocial)
            persona.save()
            personas= Persona.objects.all()
            return render(request, "AppCoder/personas.html", {"personas":personas, "mensaje": "Persona guardada correctamente"})
        else:
            return render(request, "AppCoder/agregarPersona.html", {"formulario": formulario})
    else:
        form=PersonaForm()
        return render(request, "AppCoder/agregarPersona.html", {"form": form, "mensaje":"AGREGAR PERSONA"})


def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form":form}) 