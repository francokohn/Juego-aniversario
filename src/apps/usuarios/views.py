from django.shortcuts 	import render, redirect
from .forms  			import RegistroUsuarioForm
from .models 			import Usuario

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

def nuevo_usuario(request):
	template_name = "usuarios/nuevo.html"

	if request.method == 'POST':
		form = Usuario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = Usuario()

	ctx = {
		'form': RegistroUsuarioForm()
	}
	return render (request,template_name,ctx)
