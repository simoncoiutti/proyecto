from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30)
    edad = models.IntegerField()


def __str__(self):
    return self.nombre+""+str(self.edad)+self.parentesco


class Sextuples(models.Model):
    direccion = models.CharField(max_length=30)
    empresa_vp = models.CharField(max_length=30)
    cantidad = models.IntegerField()


def __str__(self):
    return self.direccion+""+ self.empresa +str(self.cantidad)



class Empresa_vp(models.Model):
    empresa_vp = models.CharField(max_length=30)
    


def __str__(self):
    return self.direccion+""