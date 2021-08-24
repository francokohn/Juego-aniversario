from django.db import models

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    respuestas = models.ForeignField('Respuesta', on_delete=models.CASCADE,)

    #id_partida = models.ManyToManyField('Partida')

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