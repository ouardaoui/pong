"""
Django settings for authentication project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from accounts import middleware
import os



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587
EMAIL_USE_TLS = True  





EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
UID = os.getenv('UID')
SECRET = os.getenv('SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
JWT_SECRET_KEY=os.getenv('JWT_SECRET')

# SECURE_SSL_REDIRECT = True






AUTH_USER_MODEL = 'accounts.CustomUser'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6rxobww5kvupqi&2v)#)#7-0uspypmkli_5yj*+b*l(6yvdib('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'daphne',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'rest_framework_simplejwt',
    'accounts',
    'pages',
    'channels',
    'corsheaders',

]


# Configure REST Framework to use JWTAuthentication 
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Keep this first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # Only need this once
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'accounts.middleware.DisableCSRF',
    'accounts.middleware.JWTAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# If you want to be more specific about allowed origins (more secure):

# Add allowed methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Add allowed headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]



ROOT_URLCONF = 'authentication.urls'

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


ASGI_APPLICATION = 'authentication.asgi.application'
WSGI_APPLICATION = 'authentication.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'citizdeix_db',
        'USER': 'citiziddex_user',
        'PASSWORD': 'Sde3cret',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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



# MEDIA_ROOT = '/Users/yichiba/Desktop/authentication/authentication/accounts/'
# MEDIA_URL = '/media/'

MEDIA_URL = 'accounts/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'accounts/media')


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}