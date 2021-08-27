from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta
from .forms import PreguntaForm,RespuestaForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

def crear_pregunta(request):
	template_name = "preguntas/newquestion.html"

	#if request.method == "POST":
	#	texto_pregunta = request.POST.get("texto_pregunta",None)
	#	categoria =  request.POST.get("categoria",None)
	#	p = Pregunta.objects.create(texto_pregunta=texto_pregunta,categoria=categoria)
	#	return redirect('PAGINA DE PREGUNTAS LISTADAS')

	ctx = {
		'form': PreguntaForm(),
		'form1': RespuestaForm()
	}

	return render(request,template_name,ctx)

@login_required
def preguntar(request):
	template_name = "preguntas/jugar.html"
	ctx = {}

	
	print("============")
	rtas = Respuesta.objects.all()
	pregs = Pregunta.objects.all()
	for p in pregs:
		print(p.texto_pregunta)
		for r in rtas:
			if r.pregunta.id == p.id:
				print(r.texto_respuesta)
	print("============")
	
	return render (request,template_name,ctx)
