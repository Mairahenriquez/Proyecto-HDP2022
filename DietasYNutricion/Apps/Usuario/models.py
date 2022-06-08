from django.db import models

# Create your models here.

class MUsuario(models.Model):
    name = models.CharField('Nombre de usuario', max_length=50, unique = True)
    email = models.EmailField('Correo Electrónico', max_length=50, unique = True)
    password = models.CharField('Password', max_length=50, unique = True)
    rol = models.CharField('Rol', max_length=50, unique = True)

