from django import forms

class CursoForm(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=50)
    comision=forms.IntegerField(label="Comision")

class ProfeForm(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=50)
    apellido=forms.CharField(label="Apellido", max_length=50)
    email=forms.EmailField(label="Email profesor")
    profesion=forms.CharField(label="Profesion", max_length=50)

class PersonaForm(forms.Form):
    dni= forms.IntegerField(label="DNI")
    nombre= forms.CharField(label="Nombre",max_length=50)
    apellido= forms.CharField(label="Apellido",max_length=50)
    email= forms.EmailField(label="Email")
    fechaNacimiento= forms.DateField(label="Fecha de Nacimiento")
    tieneObraSocial= forms.BooleanField(label="Posee Obra Social")
