from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Paciente, Municipio, PlanAlimenticio
from django.views.generic import CreateView, ListView, UpdateView, DetailView #, DeleteView
from django.urls import reverse_lazy
from .forms import PacienteForm, PlanForm
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage
from DietasYNutricion import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'paciente/index.html')

class Pacientes(ListView):
    model = Paciente
    template_name = "paciente/gestionar.html"

class RegistrarPacientes(CreateView):
    model = Paciente
    template_name = "paciente/registrar.html"
    form_class = PacienteForm
    success_url = reverse_lazy('GestionarPaciente')

class ModificarPacientes(UpdateView):
    model = Paciente
    template_name = "paciente/editar.html"
    form_class = PacienteForm
    success_url = reverse_lazy('GestionarPaciente')

# class EliminarPacientes(DeleteView):
#     model = Paciente
#     template_name = "paciente/eliminar.html"
#     success_url = reverse_lazy('GestionarPaciente')

def load_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).all()
    return render(request, 'paciente/municipio_dropdown_list_options.html', {'municipios': municipios})

class DetallePaciente(DetailView):
    model = Paciente
    template_name = "paciente/detalle.html"

class TipoDietas(ListView):
    model = PlanAlimenticio
    template_name = "paciente/informacion.html"
    form_class = PlanForm
        
def email(request):
    if request.method == "POST":
        mail= request.POST['mail']
        paciente = Paciente.objects.filter(email=mail).all()

        if Paciente.objects.filter(email=mail).all():
            template = render_to_string('paciente/email.html',{'paciente':paciente})
                
            email = EmailMessage(
                'Dieta asignada',
                template,
                settings.DEFAULT_FROM_EMAIL,
                [mail]
            )
            
            email.fail_silently = False
            email.content_subtype = "html"
            email.send()

            messages.success(request, 'Correo enviado exitosamente')
        
        else:
            messages.error(request, 'Correo no encontrado')
            return redirect('Email')

    return render(request, 'paciente/correo.html',{})