from django.contrib import admin
from .models import Usuario

class UsuariosAdmin(admin.ModelAdmin):
	list_display = ['id','nombre','nickname','localidad','ult_acceso']

admin.site.register(Usuario, UsuariosAdmin)