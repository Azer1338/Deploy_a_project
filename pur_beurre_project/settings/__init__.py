"""
Django settings for Pur_beurre_project project.
Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'yn)%cc*v0#1c^0_l646^f-ci9p^zb7cd-@1w7uof68(t7f(5mw')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow the access to
ALLOWED_HOSTS = []

# Application definition
AUTH_USER_MODEL = 'accounts.PurBeurreUser'

INSTALLED_APPS = [
        'main.apps.MainConfig',
        'substitute.apps.SubstituteConfig',        
        'accounts.apps.AccountsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'debug_toolbar',
        'crispy_forms',
        ]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]

ROOT_URLCONF = 'pur_beurre_project.urls'

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
                    ],
                },
            },
        ]

WSGI_APPLICATION = 'pur_beurre_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
        'default': {       
            # on utilise l'adaptateur postgresql
            'ENGINE': 'django.db.backends.postgresql',
            # le nom de notre base de donnees creee precedemment
            'NAME': 'pur_beurre_db',
            # attention : remplacez par votre nom d'utilisateur
            'USER': 'azer',
            'PASSWORD': 'azerazer',
            'HOST': 'localhost',
            'PORT': '5432',
            }
        }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Crispy configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

# Django debug toolbar
INTERNAL_IPS = ['127.0.0.1']
