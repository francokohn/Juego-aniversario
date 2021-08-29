from django.urls import path
from . import views

app_name = "partidas"

urlpatterns = [
	path('jugar/', views.jugar, name="jugar"),
	path('', views.listar, name="listar"),
]