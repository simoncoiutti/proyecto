from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from appproyecto.forms import sextuplesform,empresaform,familiarform

# Create your views here.
def inicio(request):
    return render(request,"appproyecto/inicio.html")

def familiar(request):
    return render(request,"appproyecto/familiar.html")
    
    
    cadena_texto="familiar guardado"
    return render(request,"appproyecto/familiares.html",{"lista_familiares":lista_familiares})

def sextuples(request):
    
    return render(request,"appproyecto/sextuples.html")

def empresa_vp(request):
    
    return render(request,"appproyecto/empresa.html")


"""def sextuplesFormulario(request):
    if request.method=="POST":
        form= sextuplesform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            
            direccion=informacion["Direccion"]
            empresa_vp=informacion["Empresa"]
            cantidad=informacion["Cantidad"]
            sextuples= Sextuples(direccion=direccion,empresa=empresa_vp,cantidad=cantidad)
            sextuples.save
            return render(request,"appproyecto/inicio.html",{"mensaje": "Sextuple guardado correctamente"})

        else:
            return render (request," approyecto/sextuplesFormulario.html" ,{"form": form,"mensaje":"Bad Information"})
    
    else:
        formulario= sextuplesform()
        return render (request, "appproyecto/sextuplesFormulario.html",{"form":formulario})"""

def sextuplesFormulario(request):
    if request.method=="POST":
        form= sextuplesform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            
            direccion= informacion["direccion"]
            empresa_vp= informacion["empresa_vp"]
            cantidad= informacion["cantidad"]
            
            sextuples= sextuples(direccion=direccion,empresa=empresa_vp, cantidad=cantidad)
            sextuples.save()
            return render(request, "Appproyecto/inicio.html" ,{"mensaje": "Curso guardado correctamente"})
        else:
            return render(request, "Appproyecto/sextuplesFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= sextuplesform()
        return render (request, "Appproyecto/sextuplesFormulario.html", {"form": formulario})



def empresaFormulario(request):
    if request.method=="POST":
        form= empresaform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            empresa_vp=informacion["Empresa"]
        
            empresa_vp= empresa_vp(empresa=empresa_vp)
            empresa_vp.save
            return render(request,"appproyecto/inicio.html",{"mensaje": "Empresa guardada correctamente"})

        else:
            return render(request," approyecto/empresaFormulario.html" ,{"form": form,"mensaje":"Bad Information"})
    
    else:
        formulario= empresaform()
        return render (request, "appproyecto/empresaFormulario.html",{"form":formulario})


def familiarFormulario(request):
    if request.method=="POST":
        form= familiarform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["Nombre"]
            edad=informacion["Edad"]
            parentesco=informacion["Parentesco"]
            familiar= familiar(nombre=nombre,edad=edad,parentesco=parentesco)
            familiar.save
            return render(request,"appproyecto/inicio.html",{"mensaje": "Familiar guardado correctamente"})

        else:
            return render(request," approyecto/familiarFormulario.html" ,{"form": form,"mensaje":"Bad Information"})
    
    else:
        formulario= familiarform()
        return render (request, "appproyecto/familiarFormulario.html",{"form":formulario})

def busquedasextuples(request):
    return render(request,"appproyecto/busquedasextuples.html")


def buscar(request):
    if "direccion" in request.GET:
        return HttpResponse(F"ESTOY BUSCANDO LA DIRECCION {request.GET['direccion']}")