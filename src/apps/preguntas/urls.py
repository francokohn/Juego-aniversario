from django.urls import path
from . import views

app_name = "preguntas"

urlpatterns = [
	path('crear/', views.crear_pregunta, name = "crear_pregunta"),
	path('', views.preguntar, name="preguntas")
]