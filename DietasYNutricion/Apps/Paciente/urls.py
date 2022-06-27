from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name = "index"),
    path('gestionar-paciente',login_required(views.Pacientes.as_view()),name="GestionarPaciente"),
    path('registrar-paciente',login_required(views.RegistrarPacientes.as_view()),name="RegistrarPaciente"),
    path('modificar-paciente/<int:pk>/',login_required(views.ModificarPacientes.as_view()),name="ModificarPaciente"),
    # path('eliminar-paciente/<int:pk>/',login_required(views.EliminarPacientes.as_view()),name="EliminarPaciente"),
    path('ajax/load-municipios/', views.load_municipios, name='ajax_load_municipios'), # AJAX
    path('detalle_paciente/<int:pk>/', login_required(views.DetallePaciente.as_view()),name="DetallePaciente"),
    path('informacion',login_required(views.TipoDietas.as_view()),name="TipoDietas"),
    path('mail',login_required(views.email),name="Email"),
]