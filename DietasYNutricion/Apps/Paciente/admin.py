from django.contrib import admin
from .models import Paciente, Departamento, Municipio, PlanAlimenticio

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(PlanAlimenticio)