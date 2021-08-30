from django.urls import path
from . import views

app_name = "preguntas"

urlpatterns = [
	path('crear/', views.crear, name="crear"),
	path('crear/guardar', views.guardar, name="guardar"),
	path('eliminar/<int:pk>/', views.eliminar, name="eliminar"),
	path('', views.listar, name="listar"),
]