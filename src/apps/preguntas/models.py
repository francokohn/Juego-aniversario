from django.db import models
from django.db.models.deletion import CASCADE
from apps.usuarios.models import Usuario
import random

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    nivel = models.IntegerField()

    class Meta:
        db_table = 'Pregunta'

    def __str__(self):
        return self.texto_pregunta

    def get_respuestas(self):
        # traer todas las respuestas relacionadas a esta pregunta
        respuestas = self.respuesta_set
        # filtrar las incorrectas, crear una lista con sus ids y randomizarlos
        ids = [i.id for i in respuestas.filter(es_correcta = False)]
        random.shuffle(ids)
        # tomar muestra de 2 incorrectas
        subset = ids[:2]
        # buscamos la correcta
        correcta = respuestas.get(es_correcta = True)
        # agregamos el id de la correcta a la lista de incorrectas
        subset.append(correcta.id)
        # mezclamos de nuevo
        random.shuffle(subset)
        # devolvemos los objetos de los ids como nos quedaron
        return [respuestas.get(pk=i) for i in subset]

class Partida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    puntos = models.IntegerField()
   
    class Meta:
        db_table = 'Partida'

class Respuesta(models.Model):
    texto_respuesta = models.CharField(max_length=255)
    pregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
    es_correcta = models.BooleanField(default=False)

    class Meta:
        db_table = 'Respuesta'

    def __str__(self):
        return self.texto_respuesta
