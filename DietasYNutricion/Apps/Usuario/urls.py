from django.urls import path
from Apps.Usuario import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('gestionar-usuario',login_required(views.Usuarios.as_view()),name="usuario"),
    path('registrar-usuario',login_required(views.RegistrarUsuarios.as_view()),name="RegistrarUsuario"),
    path('modificar-usuario/<int:pk>/',login_required(views.ModificarUsuarios.as_view()),name="ModificarUsuario"),
    path('eliminar-usuario/<int:pk>/',login_required(views.EliminarUsuarios.as_view()),name="EliminarUsuario"),
    path('cambiar-contraseña',login_required(views.cambiar_contraseña),name="CambiarContraseña"),
]