from django import forms
from .models import Pregunta, Respuesta

class PreguntaForm (forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = [ 
			'texto_pregunta', 
			'nivel'
		]

class RespuestaForm (forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = [ 
			'texto_respuesta'
		]