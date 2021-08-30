from django.contrib import admin
#para poder utilizar los models de preguntas
from .models import Pregunta, Partida, Respuesta

class PreguntasAdmin (admin.ModelAdmin):
	list_display = [
		'id', 
		'texto_pregunta', 
		'nivel'
	]

class PartidasAdmin (admin.ModelAdmin):
	list_display = [
		'usuario', 
		'fecha', 
		'puntos'
	]

class RespuestasAdmin (admin.ModelAdmin):
	list_display = [
		'pregunta',
		'texto_respuesta',
		'es_correcta'
	]

admin.site.register(Pregunta, PreguntasAdmin)
admin.site.register(Partida, PartidasAdmin)
admin.site.register(Respuesta, RespuestasAdmin)




