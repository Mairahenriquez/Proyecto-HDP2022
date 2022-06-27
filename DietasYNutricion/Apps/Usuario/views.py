from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .mixins import ValidarPermisosRequeridosMixin
from django.urls import reverse_lazy
from .forms import UsuarioForm

# Create your views here.

class Usuarios(ValidarPermisosRequeridosMixin,ListView):
    permission_required = 'usuario.view_user'
    model = User
    template_name = "usuario/gestionar.html"

class RegistrarUsuarios(ValidarPermisosRequeridosMixin,CreateView):
    permission_required = 'usuario.add_user'
    model = User
    template_name = "usuario/registrar.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario')

class ModificarUsuarios(ValidarPermisosRequeridosMixin,UpdateView):
    permission_required = 'usuario.change_user'
    model = User
    template_name = "usuario/editar.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario')

class EliminarUsuarios(ValidarPermisosRequeridosMixin,DeleteView):
    permission_required = 'usuario.delete_user'
    model = User
    template_name = "usuario/eliminar.html"
    success_url = reverse_lazy('usuario')
