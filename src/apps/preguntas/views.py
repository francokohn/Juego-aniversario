from django.shortcuts import render
from .models import Pregunta
from .forms import PreguntaForm

def crear_pregunta(request):
	template_name = "preguntas/newquestion.html"
	#lista_de_preguntas = Pregunta.objects.all()
	#print(lista_de_preguntas)
	ctx = {
		 'form': PreguntaForm()
	}

	return render(request,template_name,ctx)