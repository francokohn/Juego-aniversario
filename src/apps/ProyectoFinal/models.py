from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    correo = models.EmailField()
    es_admin = models.BooleanField()
    localidad = models.CharField(max_length=255)
    ult_acceso = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre
