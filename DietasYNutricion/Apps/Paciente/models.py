from django.db import models

# Create your models here.

class MDepartamento(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=50)

class MMunicipio(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
