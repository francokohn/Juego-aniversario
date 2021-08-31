# Juego Aniversario
_Proyecto final para el cursado del módulo Programación Web, realizado por el grupo 8 de la comisión 4 del Informatorio._ 

## Instrucciones 📋
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


## Pre-requisitos 🖱
_Instalar las dependencias del proyecto, ir a la carpeta de requirements y poner el siguiente comando con nuestro entorno corriendo:_
```
pip install -r base.txt
```
_Luego creamos el settings 'local.py' en la carpeta "settings" y cambiamos los siguientes datos para la conexión a la DB:_
```
from .base import *
```
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
```

## Instalación 🔧
_Una vez instalados los requirements y configurado el settings nos ubicamos con el entorno en la carpeta "src"
y ejecutamos el comando 'python manage.py runserver' y listo!_

##Construido con 🛠️
* [Django]Framework web
* [PostgreSQL]Base de datos
* template base: https://getbootstrap.com/docs/4.0/examples/album/

Autores ✒️

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **@LeandroGomezz** - [Leandro Gomez](https://github.com/LeandroGomezz)
* **@francokohn** - [Franco Kohn](https://github.com/Francokohn)
* **@nadia-pisarello** - [Nadia Pisarello](https://github.com/nadia-pisarello)
* **@mainardsolis** - [Mainard Solis](https://github.com/mainardsolis)
* **@RaulVilloria** - [RaulVilloria](https://github.com/RaulVilloria)

---
Este trabajo no había sido posible sin la ayuda y la paciencia de Lucas Ibañez [@lucasibaniez](https://github.com/lucasibaniez) 🤓


