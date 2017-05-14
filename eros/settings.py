"""
Django settings for eros project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import local_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2#kr3u6s+#i$*ylm4@%#ozt_8c(0z4440ik)$q9jnmzfsw07wg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'integrations',
    'scrapers',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eros.urls'

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

WSGI_APPLICATION = 'eros.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


TWEEPY_CONSUMER_KEY = 'ZKx8Yg55evn1U65vRWQ0Zj7Jr'
TWEEPY_CONSUMER_SECRET = '26OYZDNj0hC17ei6JplHuerzoaxokQBpU9X2dsegkLLCShBK2y'
TWEEPY_ACCESS_TOKEN = '14404065-baBGgZmVoCnZEU1L0hCVq6ed6qHDFXVrLSQpAKXcw'
TWEEPY_ACCESS_TOKEN_SECRET = '3jbRjcgZV82OGLOsxv9Xg8G29h1oc9l9kqKTMXH4vEPNi'

FACEBOOK_ID = '100007032789992'
FACEBOOK_AUTH_TOKEN = "fbconnect://success#access_token=EAAGm0PX4ZCpsBAPGZBrXsQAh6ZAYCBRqcWwXJyZAPameyeTcZAxVSd8FhtLt5JQdmZCwRL2OczZAZBNPofGCGWy4oyGzXPVdWnIwfU4eWN31SXRpEd5oCPHZCWvW4gyLZAOOhvZBIrJaQd3HgzZBtekCtfZADYHn3tO8tZCqlZCJtkVc3gGrF3ZCrbos8ZB0BZAXvqPnknhK4ZD&expires_in=6277"


USER_TOKEN = "<<user>>"
LINK_TOKEN = "<<link>>"
TAG_TOKEN = "<<tag>>"

INSTAGRAM_USERNAME = local_settings.instagram_username
INSTAGRAM_PASSWORD = local_settings.instagram_password
INSTAGRAM_ACCOUNT_USERNAME = local_settings.instagram_account_username

CURRENT_TINDER_EXPERIMENT_NO = 0
TINDER_EXPERIMENT_NO = 3
