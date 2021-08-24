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
    idusuario = models.ForeignKey('Usuario2', on_delete=models.CASCADE,)
    fecha = models.DateField()
    preguntas = models.ManyToManyField('Pregunta')

    class Meta:
        db_table = 'partida'

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    id_partida = models.ManyToManyField('Partida')
    respuestas = models.ForeignField('Respuesta', on_delete=models.CASCADE,)

    class Meta:
        db_table = 'pregunta'

    def __str__(self):
        return self.nombre


class Respuesta(models.Model):
    id_pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE,)
    es_correcta = models.BooleanField()
    texto_respuesta = models.CharField(max_length=255)

    class Meta:
        db_table = 'respueta'

    def __str__(self):
        return self.nombre
