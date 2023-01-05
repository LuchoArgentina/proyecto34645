from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor
from AppCoder.forms import CursoForm, ProfeForm

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
            return render(request, "AppCoder/cursoFormulario.html", {"form1":form, "mensaje": "Info no valida"})

    else:
        formulario=CursoForm()
        return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario})


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
            return render(request, "AppCoder/inicio.html", {"mensaje": "Profe guardado correctamente"})
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
    return render(request, "AppCoder/profesores.html", {"profesores": profesores})


def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)  #Cuando llamo al profe, me lo trae, para luego eliminar.
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "AppCoder/Profesores.html", {"profesor":profesores,"mensaje":"Profesor eliminado correctamente"})


def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id) #Traje al profe que quiero editar
    if request.method=="POST":
        pass
    else:
        formulario= ProfeForm(initial={"nombre":profesor.nombre,"apellido":profesor.apellido,"email":profesor.email,"profesion":profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html",{"form":formulario,"profesor":profesor} )  
    