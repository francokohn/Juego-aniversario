from django.contrib import admin
#para poder utilizar los models de preguntas
from preguntas.models import Pregunta, Respuesta

# Register your models here.
# para que el admin puedar gestionarlo
admin.site.register(Pregunta)
admin.site.register(Respuesta)

