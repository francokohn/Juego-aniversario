Juego Aniversario
Proyecto final para el cursado del módulo Programación Web, realizado por el grupo 8 de la comisión 4 del Informatorio. 

Instrucciones 📋
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


Pre-requisitos 🖱
Instalar las dependencias del proyecto, ir a la carpeta de requirements y poner el siguiente comando con nuestro entorno corriendo:

pip install -r base.txt

Luego creamos el settings 'local.py' en la carpeta "settings" y cambiamos los siguientes datos para la conexión a la DB:

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'NombreBaseDeDatos',
        'USER': 'UsuarioBaseDeDatos',
        'PASSWORD': 'ContraseñaBaseDeDatos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

Instalación 🔧
Una vez instalados los requirements y configurado el settings nos ubicamos con el entorno en la carpeta "src"
y ejecutamos el comando 'python manage.py runserver' y listo!

Construido con 🛠️
[Django]Framework web
[PostgreSQL]Base de datos

Autores ✒️
@LeandroGomezz - [Leandro Gomez]
@francokohn - [Franco Kohn]
@nadia-pisarello - [Nadia Pisarello]
@mainardsolis - [Mainard Solis]
@RaulVilloria - [RaulVilloria]


Este trabajo no había sido posible sin la ayuda y la paciencia de Lucas Ibañez [@lucasibaniez] 🤓


