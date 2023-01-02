from django.urls import path
from appproyecto import views
from django.contrib import admin

urlpatterns = [
	
	path("familiar/", views.familiar, name="familiar"),
	path("sextuples/", views.sextuples, name="sextuples"),
	path("empresa/", views.empresa_vp, name="empresa"),
	path("inicio/", views.inicio, name="inicio"),
	path("sextuplesFormulario/", views.sextuplesFormulario, name="sextuplesFormulario"),
	path("empresaFormulario/", views.empresaFormulario, name="empresaFormulario"),
	path("familiarFormulario/", views.familiarFormulario, name="familiarFormulario"),
	path("busquedasextuples/", views.busquedasextuples, name="busquedasextuples"),
	path("buscar/", views.buscar, name="buscar"),
	]
