from django.shortcuts import render


def inicio(request):
	template_name = "inicio.html"

	lista_alumnos = [
		"Alumno 1",
		"Alumno 2"
	]

	ctx = {
		'username': "Franco",
		"Lista": lista_alumnos
	}	

	return render(request,template_name,ctx)