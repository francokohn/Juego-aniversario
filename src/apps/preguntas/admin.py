from django.contrib import admin
#para poder utilizar los models de preguntas
from .models import Pregunta, Respuesta

class PreguntasAdmin (admin.ModelAdmin):
	list_display = ['id','texto_pregunta','categoria']

# para que el admin puedar gestionarlo
admin.site.register(Pregunta,PreguntasAdmin)
admin.site.register(Respuesta)

