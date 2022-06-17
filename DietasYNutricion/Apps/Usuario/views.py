from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your views here.

class Usuarios(ListView):
    model=User
    template_name="usuario/gestionar.html"

class RegistrarUsuarios(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('Usuario')

class ModificarUsuarios(UpdateView):
    model=User
    template_name="usuario/editar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Usuario')

class EliminarUsuarios(DeleteView):
    model=User
    template_name = "usuario/eliminar.html"
    success_url = reverse_lazy('Usuario')

