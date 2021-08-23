from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Proyecto',
        'USER': 'postgres',
        'PASSWORD': 'asd123',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}
