"""
Configuración de Django para el proyecto ProyectoWeb.

Generado por 'django-admin startproject' utilizando Django 5.0.6.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.0/topics/settings/

Para ver la lista completa de configuraciones y sus valores, consulta
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

from django.contrib.messages import constants as mensajes_de_error

# Construye las rutas dentro del proyecto de esta manera: BASE_DIR / 'subdirectorio'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración rápida para desarrollo; no adecuada para producción
# Consulta https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantén secreta la clave utilizada en producción!
SECRET_KEY = 'django-insecure-2h_%7n58-!a+*l!uyi&w_=9+%@^(9#0cal(z(7!6-9ikpag=lw'

# ADVERTENCIA DE SEGURIDAD: no ejecutes con DEBUG activado en producción.
DEBUG = True  # Cuando despliegues el proyecto, debe ser False; mientras desarrollas, True.

ALLOWED_HOSTS = ['*']

# Definición de las aplicaciones del proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProyectoWebApp',
    'capsulas',
    'solicitudes',
    'contacto',
    'autenticacion',
]
   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoWeb.wsgi.application'

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cocacolaandina_resiter',
        'USER': 'root',  # Nombre de usuario de MySQL
        'PASSWORD': '',  # Contraseña de MySQL
        'HOST': 'localhost',  # Puedes cambiar esto si tu base de datos está en un servidor remoto
        'PORT': '3306',  # Puerto de MySQL por defecto
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es'  # Cambiamos el idioma a español
TIME_ZONE = 'America/Punta_Arenas'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, '/static'), )

# Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')  # Todos los elementos cargables se guardarán aquí desde la base de datos

# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'pruebacocacolaandinaresiter@gmail.com'
EMAIL_HOST_PASSWORD = 'prcz tmoa cvas odcc'  # Contraseña de Aplicaciones de Prueba (Gmail)

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS={
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}

AUTH_USER_MODEL = 'autenticacion.Usuario_Registro'