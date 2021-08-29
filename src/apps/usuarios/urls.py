from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
	path('', views.inicio, name='inicio'),
    path('login/', views.loguear, name="login"),
    path('logout/', views.desloguear, name="logout"),
    path('registro/', views.registrar_usuario, name="registro"),
	path('usuarios/', views.listar_usuarios, name="listar"),
	path('usuarios/crear/', views.crear_usuario, name="crear_usuario"),
]