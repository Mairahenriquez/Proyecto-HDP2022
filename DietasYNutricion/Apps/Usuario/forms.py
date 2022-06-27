from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):

	class Meta:
		model = User
		fields =  [
				'username',
				'first_name',
				'last_name',
				'email',
				'is_superuser',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Dirección de correo electronico',
				'is_superuser': '¿Es administrador?'
		}
