from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def inicio(request):
    return render(request,"appproyecto/inicio.html")

def familiar(request):
    familiar1= Familiar(nombre="Maria Delia", edad=66 ,parentesco="madre")
    familiar1.save()
    familiar2= Familiar(nombre="Ignacio", edad=32 ,parentesco="hermano")
    familiar2.save()
    familiar3= Familiar(nombre="Emi", edad=7 ,parentesco="hija")
    familiar3.save()
    
    lista_familiares=[familiar1,familiar2,familiar3]
    
    cadena_texto="familiar guardado"
    return render(request,"appproyecto/familiares.html",{"lista_familiares":lista_familiares})

def sextuples(request):
    
    return render(request,"appproyecto/sextuples.html")

def empresa(request):
    
    return render(request,"appproyecto/empresa.html")


def sextuplesFormulario(request):
    if request.method=="POST":
        direccion= request.POST["direccion"]
        empresa= request.POST["Empresa VP"]
        cantidad= request.POST["cantidad"]
        sextuples= Sextuples(direccion=direccion,empresa=empresa,cantidad=cantidad)
        sextuples.save
        return render(request,"appproyecto/inicio.html" ,{"mensaje": "Sextuples guardados correctamente"})
    else:
        return render(request,"appproyecto/sextuplesFormulario.html")


def empresaFormulario(request):
    return render(request,"appproyecto/empresaFormulario.html")