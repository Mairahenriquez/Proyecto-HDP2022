from django import forms
from .models import Paciente, PlanAlimenticio

class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = "__all__"

class PlanForm(forms.ModelForm):
	class Meta:
		model = PlanAlimenticio
		fields = "__all__"