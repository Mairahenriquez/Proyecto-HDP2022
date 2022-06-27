from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
	first_name = forms.CharField(label='Nombre', max_length=30, required=True)
	last_name = forms.CharField(label='Apellidos', max_length=30, required=True)
	email = forms.EmailField(label='Dirección de correo electronico' ,max_length=254, required=True)
	
	class Meta:
		model = User
		fields = [
				'username', 
				'first_name', 
				'last_name', 
				'email', 
				'is_superuser', 
				'password1', 
				'password2', 
			]
		labels = {
				'is_superuser': '¿Es administrador?'
		}

class ModificarUsuarioForm(UserChangeForm):
	password = None
	first_name = forms.CharField(label='Nombre', max_length=30, required=True)
	last_name = forms.CharField(label='Apellidos', max_length=30, required=True)
	email = forms.EmailField(label='Dirección de correo electronico' ,max_length=254, required=True)
	
	class Meta:
		model = User
		fields = [
				'username', 
				'first_name', 
				'last_name', 
				'email', 
				'is_superuser',
			]
		labels = {
				'is_superuser': '¿Es administrador?'
		}
