from django.db import models

# Create your models here.


class Usuario2(models.Model):
    nombre = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    es_admin = models.BooleanField()
    puntaje = models.IntegerField()
    ult_acceso = models.DateField()
    partidas = models.ForeignKey('Partida', on_delete=models.CASCADE,)


class Partida(models.Model):
    puntos = models.IntegerField()
    cnt_respondidas = models.IntegerField()
    idusuario = models.ForeignKey('Usuario2',  on_delete=models.CASCADE,)
    fecha = models.DateField()
    preguntas = models.ForeignKey('Pregunta', on_delete=models.CASCADE,)
    

class Pregunta(models.Model):
    id_partida = models.ForeignKey('Partida', on_delete=models.CASCADE,)
    respuestas = models.ForeignKey('Respuesta', on_delete=models.CASCADE,)


class Respuesta(models.Model):
    id_pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE,)
    es_correcta = models.BooleanField()
