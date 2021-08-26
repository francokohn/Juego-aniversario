from django.shortcuts import render, redirect
from .models import Pregunta
from .forms import PreguntaForm
from django.views.generic import CreateView

def crear_pregunta(request):
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