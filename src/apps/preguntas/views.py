from django.shortcuts import render

def crear_pregunta(request):
	template_name = "preguntas/newquestion.html"
	ctx = { }

	return render(request,template_name,ctx)