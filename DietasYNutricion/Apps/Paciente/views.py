from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Paciente, Municipio
from django.views.generic import CreateView, ListView, UpdateView #, DeleteView
from django.urls import reverse_lazy
from .forms import PacienteForm

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
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

class DetallePaciente(ListView):
    model = Paciente
    template_name = "paciente/detalle.html"
    form_class = PacienteForm