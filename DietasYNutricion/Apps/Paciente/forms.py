from django import forms
from .models import Paciente, PlanAlimenticio

class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = "__all__"
		widgets = {
			'email': forms.TextInput(attrs={'placeholder': 'muestra@email.com'}),
			'dui': forms.TextInput(attrs={'placeholder': 'Ingrese número de dui sin el guión'}),
			'estatura': forms.TextInput(attrs={'placeholder': 'Ingrese la estatura en centimetros ej. 175'}),
			'peso': forms.TextInput(attrs={'placeholder': 'Ingrese el peso en kilogramos ej. 75.50'}),
        }

class PlanForm(forms.ModelForm):
	class Meta:
		model = PlanAlimenticio
		fields = "__all__"