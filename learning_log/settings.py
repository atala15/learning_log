"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v_3nkmo18ma+-8c*kx30n$wdx6mlfv9*)!l01xbn9(=41_=rlv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#  'learning_log.herokuapp.com'
ALLOWED_HOSTS = ['127.0.0.1:8000',
'127.0.0.1',
'peaceful-meadow-63182.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'bootstrap4',

    # My apps
    'learning_logs',
    'users',
    'welcome',
    # 'herokuapp',
    'lists',
    # 'accounts',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_log.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
# STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'

# # Extra lookup directories for collectstatic to find static files
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# My settings
LOGIN_URL = '/users/login'

# Heroku settings.
# cwd = os.getcwd()
# if cwd == '/app' or cwd[:4] == '/tmp':
#     import dj_database_url
#     DATABASES = {
#         'default': dj_database_url.config(default='postgres://localhost')
#     }
#     # Honor the 'X-Forwarded-Proto' header for request.is_secure().
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#     # Allow all host headers.
#     ALLOWED_HOSTS = ['*']

#     # Static asset configuration
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     STATIC_ROOT = 'staticfiles'
#     STATICFILES_DIRS = (
#         os.path.join(BASE_DIR, 'static'),
#     )

# import dj_database_url 
# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)