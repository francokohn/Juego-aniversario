# Juego Aniversario
_Proyecto final para el cursado del m贸dulo Programaci贸n Web, realizado por el grupo 8 de la comisi贸n 4 del Informatorio._ 

## Instrucciones 馃搵
_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._


## Pre-requisitos 馃柋
_Instalar las dependencias del proyecto, ir a la carpeta de requirements y poner el siguiente comando con nuestro entorno corriendo:_
```
pip install -r base.txt
```
_Luego creamos el settings 'local.py' en la carpeta "settings" y cambiamos los siguientes datos para la conexi贸n a la DB:_

from .base import *
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'NombreBaseDeDatos',
        'USER': 'UsuarioBaseDeDatos',
        'PASSWORD': 'Contrase帽aBaseDeDatos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

## Instalaci贸n 馃敡
_Una vez instalados los requirements y configurado el settings nos ubicamos con el entorno en la carpeta "src"
y ejecutamos el comando 'python manage.py runserver' y listo!_

## Construido con 馃洜锔?
* [Django]Framework web
* [PostgreSQL]Base de datos

## Autores 鉁掞笍
* **@LeandroGomezz** - [Leandro Gomez](https://github.com/LeandroGomezz)
* **@francokohn** - [Franco Kohn](https://github.com/Francokohn)
* **@nadia-pisarello** - [Nadia Pisarello](https://github.com/nadia-pisarello)
* **@mainardsolis** - [Mainard Solis](https://github.com/mainardsolis)
* **@RaulVilloria** - [RaulVilloria](https://github.com/RaulVilloria)

---
Este trabajo no hab铆a sido posible sin la ayuda y la paciencia de Lucas Iba帽ez [@lucasibaniez](https://github.com/lucasibaniez) 馃


