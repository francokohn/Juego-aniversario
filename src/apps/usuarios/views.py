from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, CrearUsuarioForm
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

RUTA_INICIO = 'usuarios:inicio'
RUTA_LOGIN = 'usuarios:login'
RUTA_LISTAR_USUARIOS = 'usuarios:listar'

def es_admin(usuario):
	return usuario.es_admin

@login_required()
@user_passes_test(es_admin, login_url = '', redirect_field_name = None)
def listar_usuarios (request):
	template_name = "usuarios/listar.html"
	usuarios = Usuario.objects.all()
	
	#para ver en consola los usuarios pasados (tamb lo puedo listar con un for)
	#print(lista_de_usuarios)

	#traer un usuario en especifico, ejemplo id=1
	#lista_de_usuarios = Usuario.objects.filter(id=1)

	ctx = {
		'usuarios': usuarios
	}	

	return render(request,template_name,ctx)

@login_required()
@user_passes_test(es_admin, login_url = '', redirect_field_name = None)
def crear_usuario(request):
	template_name = "usuarios/crear.html"
	form = CrearUsuarioForm()

	if request.method == 'POST':
		form = CrearUsuarioForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'La cuenta se ha creado exitosamente')
			return redirect(RUTA_LISTAR_USUARIOS)
		else:
			print(form.errors)

	ctx = { 'form': form }
	
	return render(request, template_name, ctx)


@login_required()
def inicio(request):
	template_name = "usuarios/inicio.html"
	return render(request, template_name, {})

def loguear(request):
    if request.user.is_authenticated:
        return redirect(RUTA_INICIO)

    if request.method=='POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            url = RUTA_LISTAR_USUARIOS if user.es_admin else RUTA_INICIO
            print(url)
            return redirect(url)
        else:
            print('Usuario incorrecto')
            messages.error(request,'Usuario o Password incorrecto')

    return render(request, "usuarios/login.html")

def registrar_usuario(request):
	if request.user.is_authenticated:
		return redirect(RUTA_INICIO)

	template_name = "usuarios/registro.html"
	form = RegistroUsuarioForm()

	if request.method == 'POST':
		form = RegistroUsuarioForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'Su cuenta se ha creado exitosamente')
			return redirect(RUTA_LOGIN)
		else:
			print(form.errors)

	ctx = { 'form': form }
	
	return render(request, template_name, ctx)

@login_required()
def desloguear(request):
    logout(request)
    return redirect(RUTA_LOGIN)