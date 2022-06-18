from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = User
		fields =  [
				'username',
				'first_name',
				'last_name',
				'email',
				'password',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
				'password': 'Contraseña',
		}
