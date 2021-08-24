from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
	nickname = models.CharField(max_length=100, null=True, blank=True)
	localidad = models.CharField(max_length=255, null=True, blank=True)
	puntos = models.IntegerField(null=True, blank=True)
	es_admin = models.BooleanField(default=False)
	ult_acceso = models.CharField(max_length=200, null=True, blank=True)

	#partidas = models.ForeignKey('Partida', on_delete=models.CASCADE,)

	class Meta:
		db_table = 'usuario'


	""""
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
	""" 