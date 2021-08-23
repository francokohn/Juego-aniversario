from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
	nickname = models.CharField(max_length=100, null=True, blank=True)
	localidad = models.CharField(max_length=255, null=True, blank=True)
	puntos = models.IntegerField(null=True, blank=True)

	class Meta:
		db_table = 'usuario'



