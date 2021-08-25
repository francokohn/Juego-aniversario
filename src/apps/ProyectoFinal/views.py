from django.shortcuts import render
from .models import Usuario

def listar_usuarios (request):
	template_name = "usuarios/listar.html"
	lista_de_usuarios = Usuario.objects.all()
	
	#para ver en consola los usuarios pasados (tamb lo puedo listar con un for)
	#print(lista_de_usuarios)

	#traer un usuario en especifico, ejemplo id=1
	#lista_de_usuarios = Usuario.objects.filter(id=1)

	ctx = {
		'usuarios' : lista_de_usuarios
	}	

	return render(request,template_name,ctx)