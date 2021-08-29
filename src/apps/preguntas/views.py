from django.shortcuts import render, redirect
from .models import Pregunta
from .forms import PreguntaForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.user_test import es_admin

@login_required()
@user_passes_test(es_admin, login_url = '', redirect_field_name = None)
def listar(request):
	template_name = "preguntas/listar.html"
	preguntas = Pregunta.objects.all()

	ctx = {
		'preguntas' : preguntas
	}	

	return render(request, template_name, ctx)

@login_required
@user_passes_test(es_admin, login_url = '/preguntas/', redirect_field_name = None)
def crear(request):
	template_name = "preguntas/newquestion.html"

	#if request.method == "POST":
	#	texto_pregunta = request.POST.get("texto_pregunta",None)
	#	categoria =  request.POST.get("categoria",None)
	#	p = Pregunta.objects.create(texto_pregunta=texto_pregunta,categoria=categoria)
	#	return redirect('PAGINA DE PREGUNTAS LISTADAS')

	ctx = {
		'form': PreguntaForm()
	}

	return render(request,template_name,ctx)

@login_required
def preguntar(request):
	template_name = "preguntas/jugar.html"
	lista_de_preguntas = Pregunta.objects.all()
	ctx = {
		'preguntas': lista_de_preguntas
	}
	
	return render (request,template_name,ctx)
