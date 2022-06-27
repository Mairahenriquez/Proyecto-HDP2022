from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator

# Create your models here.

class Departamento(models.Model):
    name = models.CharField(max_length=40, unique = True, blank = False)

    def __str__(self):
        return self.name

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, unique = True, blank = False)

    def __str__(self):
        return self.name

class PlanAlimenticio(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length = 30, blank = False, null = False)
    tiempo = models.CharField(max_length = 2, blank = False, null = False)
    descripcion = RichTextField()
    cantCarbohidratos = models.DecimalField(max_digits = 4, decimal_places = 2, blank = False, null = False)
    cantProteina = models.DecimalField(max_digits = 4, decimal_places = 2, blank = False, null = False)
    cantGrasas = models.DecimalField(max_digits = 4, decimal_places = 2, blank = False, null = False)
    cantVitaminas = models.DecimalField(max_digits = 4, decimal_places = 2, blank = False, null = False)
    cantMinerales = models.DecimalField(max_digits = 4, decimal_places = 2, blank = False, null = False)

    def __str__(self):
        return self.tipo + ", " + self.tiempo + " semanas"

class Paciente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    apellidos = models.CharField(max_length = 50, blank = False, null = False)
    email = models.EmailField(max_length=50)
    edad =  models.CharField(validators=[RegexValidator(regex='^\d{2}$', message='Cantidad de digitos insuficientes o ingreso alguna letra', code='nomatch')], max_length = 2, blank = False, null = False)
    dui = models.CharField(validators=[RegexValidator(regex='^\d{9}$', message='Cantidad de digitos insuficientes o ingreso alguna letra', code='nomatch')], max_length = 9, blank = False, null = False, unique = True)
    estatura = models.CharField(validators=[RegexValidator(regex='^\d{3}$', message='Cantidad de digitos insuficientes o ingreso alguna letra', code='nomatch')], max_length = 3, blank = False, null = False)
    peso = models.CharField(validators=[RegexValidator(regex='^\d+\.\d{2}$', message='Cantidad de digitos insuficientes o ingreso alguna letra', code='nomatch')], max_length = 5, blank = False, null = False)
    enfermedades = models.TextField(blank = False, null = False)
    afecciones = models.TextField(blank = False, null = False)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=False, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=False, null=True)
    plan = models.ForeignKey(PlanAlimenticio, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos