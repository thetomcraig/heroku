import os
"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i516twdc1fp+iq40=@&v7572(6*$r%q-d#a(rf7l0y_6h_j#(d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#For Heroku also
SESSION_ENGINE= 'django.contrib.sessions.backends.cached_db'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scrapers',
    'social.apps.django_app.default',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'scrapers/templates/scrapers')],
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#Sessions issue
import dj_database_url
in_heroku = False
if 'DATABASE_URL' in os.environ:
    in_heroku = True

if in_heroku:
    DATABASES = {'default': dj_database_url.config()}
else:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'eros',
          'USER': 'tom',
          'PASSWORD': 'Zork69105',
          'HOST': 'localhost',
          'PORT': '',
      }
  }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
  os.path.join(PROJECT_ROOT, 'static'),
)

#Defaults to the HEROKU credentials
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_FACEBOOK_KEY = '519570741529969'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd631e5a29ee38b65466059c4014bf741'


#Do I need these?
#Only local I think
"""
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_KEY = '1736382553252283'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd16e9c0762201b306380f9ad3fb12f03'
"""
