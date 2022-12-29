from django.urls import path
from appproyecto import views
from django.contrib import admin

urlpatterns = [
	path("admin" ,admin.site.urls),
	path("familiar/", views.familiar, name="familiar"),
	path("sextuples/", views.sextuples, name="sextuples"),
	path("empresa/", views.empresa, name="empresa"),
	path("inicio", views.inicio, name="inicio"),
	path("sextuplesFormulario", views.sextuplesFormulario, name="sextuplesFormulario"),
	path("empresaFormulario", views.empresaFormulario, name="empresaFormulario"),
	]
