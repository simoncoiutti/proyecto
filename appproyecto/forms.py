from django import forms

class sextuplesform(forms.Form):
    direccion= forms.CharField(label="Direccion" ,max_length=40)
    empresa_vp= forms.CharField(label="Empresa" ,max_length=20)
    cantidad= forms.IntegerField(label="Cantidad")

class empresaform(forms.Form):
    empresa_vp= forms.CharField(label="Empresa" ,max_length=20)
    
class familiarform(forms.Form):
    nombre= forms.CharField(label="Nombre" ,max_length=40)
    edad= forms.IntegerField(label="Edad")
    parentesco= forms.CharField(label="Perentesco", max_length=20)
