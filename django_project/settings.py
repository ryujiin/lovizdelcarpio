"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps de terceros
    'rest_framework',
    'rest_framework.authtoken',
    'sorl.thumbnail',
    #'mailchimp',
    'storages',
    'gunicorn',
    #mis apps
    'carro',
    'cliente',
    'catalogo',
    'contabilidad',
    'cmsloviz',
    'desboard',
    'pedido',
    'material',
    'ubigeo',
    'tienda',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': config.PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = location("public/media")
MEDIA_URL = '/media/'

STATIC_ROOT = location('public/static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    location('templates'),
)

#AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
#AWS_STORAGE_BUCKET_NAME = 'delcarpio'
#S3_URL = config.S3_URL
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

try:
    from .local import *
except ImportError:
    pass