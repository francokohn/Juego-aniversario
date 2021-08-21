from django.shortcuts import render

def listar_usuarios (request):
	template_name = "usuarios/listar.html"

	ctx = {
	}	

	return render(request,template_name,ctx)