from django.urls import path
from Apps.Usuario import views

urlpatterns = [
    path('Usuario',views.Usuarios.as_view(),name="Usuario"),
    path('registrar-usuario',views.RegistrarUsuarios.as_view(),name="RegistrarUsuario"),
    path('modificar-usuario/<int:pk>/',views.ModificarUsuarios.as_view(),name="ModificarUsuario"),
    path('eliminar-usuario/<int:pk>/',views.EliminarUsuarios.as_view(),name="EliminarUsuario")
]