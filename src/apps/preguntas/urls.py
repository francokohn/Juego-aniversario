from django.urls import path
from . import views

app_name = "preguntas"
urlpatterns = [
	path('Crear/',views.crear_pregunta)

]