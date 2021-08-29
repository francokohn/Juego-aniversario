from django.contrib import admin
#para poder utilizar los models de preguntas
from .models import Pregunta, Partida

class PreguntasAdmin (admin.ModelAdmin):
	list_display = [
		'id', 
		'texto_pregunta', 
		'respuesta_correcta', 
		'respuesta_incorrecta_1', 
		'respuesta_incorrecta_2'
	]

class PartidasAdmin (admin.ModelAdmin):
	list_display = [
		'usuario', 
		'fecha', 
		'puntos'
	]

admin.site.register(Pregunta, PreguntasAdmin)
admin.site.register(Partida, PartidasAdmin)



