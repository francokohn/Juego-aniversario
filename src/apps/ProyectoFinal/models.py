from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=255)
	nickname = models.CharField(max_length=50)
	correo = models.EmailField
	es_admin = models.BooleanField
	localidad = models.CharField(max_length=255)
	ult_acceso = models.CharField(max_length=255)
	puntos = models.IntegerField

	class Meta:
		db_table = 'usuarios'