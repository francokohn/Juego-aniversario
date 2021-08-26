from django import forms
from .models import Pregunta,Respuesta

class PreguntaForm (forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = [ "texto_pregunta","categoria"]


class RespuestaForm (forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ["texto_respuesta","es_correcta"]