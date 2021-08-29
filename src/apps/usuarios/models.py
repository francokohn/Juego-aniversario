from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    es_admin = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'usuario'
	
