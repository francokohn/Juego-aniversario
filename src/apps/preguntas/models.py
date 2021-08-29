from django.db import models
from django.db.models.deletion import CASCADE
from apps.usuarios.models import Usuario

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)
    respuesta_incorrecta_1 = models.CharField(max_length=255)
    respuesta_incorrecta_2 = models.CharField(max_length=255)

    class Meta:
        db_table = 'Pregunta'

    def __str__(self):
        return self.texto_pregunta

class Partida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    puntos = models.IntegerField()

    class Meta:
        db_table = 'Partida'