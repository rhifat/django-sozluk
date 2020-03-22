"""
Django settings for djdict project.

Generated by 'django-admin startproject' usign Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Set your secret key in environment variables, in development you can use a string right away for convenience
SECRET_KEY = os.environ.get("SECRET_KEY", "Not a secret! Delete this arg in production!")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: don't allow any other hosts except your real host in production!
ALLOWED_HOSTS = ['192.168.2.253', '127.0.0.1']


GRAPHENE = {
    'SCHEMA': 'dictionary_graph.schema.schema'
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Main apps
    'dictionary',
    'dictionary_graph',

    # Third Party
    'graphene_django',
    'widget_tweaks',

    # Django built-in
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dictionary.middleware.users.NoviceActivityMiddleware',
    'dictionary.middleware.frontend.MobileDetectionMiddleware'
]

ROOT_URLCONF = 'djdict.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dictionary.utils.context_processors.header_categories',
                'dictionary.utils.context_processors.left_frame',
            ],
        },
    },
]

WSGI_APPLICATION = 'djdict.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get("SOZLUK_DB_NAME"),
#         'USER': os.environ.get("SOZLUK_DB_USER"),
#         'PASSWORD': os.environ.get("SOZLUK_DB_PASSWORD"),
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# Extra

AUTH_USER_MODEL = 'dictionary.Author'
LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'Europe/Istanbul'

SESSION_COOKIE_AGE = 1209600
SESSION_ENGINE = 'dictionary.backends.session_backend'

# in development environment use Python's local mail server
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
PASSWORD_RESET_TIMEOUT_DAYS = 1  # deprecated in django 3.1
LOGIN_URL = "/login/"

USE_I18N = True

USE_L10N = True

USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
LOGIN_REDIRECT_URL = '/'
STATIC_URL = '/static/'
