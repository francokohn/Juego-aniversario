from django.db import models


CEL_CHOICES = (
    #Pimer elemento BD, segundo para mostrar
    ("CULTURA Y ARTE","Cultura y Arte"),
    ("HISTORIA","Historia"),
    ("DEPORTE","Deporte"),
    ("GEOGRAFIA","Geografia"),
    ("ECONOMIA","Economia"),
    ("CIENCIA Y EDUCACION","Ciencia y Educacion"),
    ("ENTRETENIMIENTO","Entretenimieto")
)

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255,null=True,blank=True, choices=CEL_CHOICES)
    #respuestas = models.ForeignField('Respuesta', on_delete=models.CASCADE,)
    #id_partida = models.ManyToManyField('Partida')
    #puntos = models.
    #partidas = models.ManyToManyField(partida, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Pregunta'

    def __str__(self):
        return self.texto_pregunta


class Respuesta(models.Model):
    pregunta = models.ForeignKey('pregunta', on_delete=models.CASCADE)
    es_correcta = models.BooleanField()
    texto_respuesta = models.CharField(max_length=255)

    class Meta:
        db_table = 'Respueta'

    def __str__(self):
        return self.texto_respuesta


class Partida(models.Model):
    #id_usuario = models.ManyToManyField('usuario')
    fecha = models.DateTimeField()
    puntos = models.IntegerField()
    cnt_respondidas = models.IntegerField()
    preguntas = models.ManyToManyField(Pregunta, related_name="preguntas")

    class Meta:
        db_table = 'Partida'
