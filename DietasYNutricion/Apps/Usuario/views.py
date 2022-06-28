from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .mixins import ValidarPermisosRequeridosMixin
from django.urls import reverse_lazy
from .forms import UsuarioForm, ModificarUsuarioForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib import messages

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
    form_class = ModificarUsuarioForm
    success_url = reverse_lazy('usuario')

class EliminarUsuarios(ValidarPermisosRequeridosMixin,DeleteView):
    permission_required = 'usuario.delete_user'
    model = User
    template_name = "usuario/eliminar.html"
    success_url = reverse_lazy('usuario')

def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('usuario')
        else:
            messages.error(request, 'Su nueva contraseña no cumple con los requerimientos')
            return redirect('CambiarContraseña')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'usuario/cambiarcontraseña.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Su nombre de usuario o contraseña son incorrectos"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
    