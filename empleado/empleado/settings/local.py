from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

""" #CONEXION CON BD EN LA MAQUINA DE OFICINAS
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'test2',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : '10.10.1.202',
        'PORT' : 3306
    }
}"""
#CONEXION CON LA BD EN EL SERVIDOR DO
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'testpapdo',
        'USER' : 'adminpap',
        'PASSWORD' : 'rsaM8pap_',
        'HOST' : '137.184.27.227',
        'PORT' : 3306
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')