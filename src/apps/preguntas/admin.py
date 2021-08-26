from django.contrib import admin
#para poder utilizar los models de preguntas
from .models import Pregunta, Respuesta, Partida

class PreguntasAdmin (admin.ModelAdmin):
	list_display = ['id','texto_pregunta','categoria']
admin.site.register(Pregunta,PreguntasAdmin)


class RespuestasAdmin (admin.ModelAdmin):
	list_display = ['pregunta','es_correcta','texto_respuesta']
admin.site.register(Respuesta,RespuestasAdmin)

class PartidasAdmin (admin.ModelAdmin):
	list_display = ['fecha','puntos','cnt_respondidas']
admin.site.register(Partida,PartidasAdmin)



