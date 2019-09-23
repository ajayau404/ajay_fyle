"""
Django settings for ajay_fyle project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR 		= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY 		= 'v4tbcvf1@vv!6rxg*xgdr2$#tma6b!zgc&sdv3-ih@f#w%+970'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG 			= False # True # 
ALLOWED_HOSTS 	= ['13.235.87.235']

DB_NAME 		= 'bank'
DB_USER_NAME 	= 'postgres'
DB_PASSWORD 	= 'toor'
DB_HOST 		= 'localhost'
DB_PORT 		= ''
JWT_SECRET_KEY	= SECRET_KEY
ISPROD 			= "dev"
try:
	ISPROD = os.environ['ISPROD']
except Exception as e:
	print("Env variables not found. Exception:%s"%(e))
# print("ISPROD:",os.environ['ISPROD'])
if ISPROD.upper() == "PROD": ## For production
	try:
		SECRET_KEY 		= os.environ['DJANGO_KEY']
		DEBUG 			= False
		DB_NAME 		= os.environ['DB_NAME']
		DB_USER_NAME 	= os.environ['DB_USER_NAME']
		DB_PASSWORD 	= os.environ['DB_PASSWORD']
		DB_HOST 		= os.environ['DB_HOST']
		DB_PORT 		= os.environ['DB_PORT']
		JWT_SECRET_KEY	= os.environ['JWT_SECRET_KEY']
	except Exception as e:
		print("Env variables not found. Exception:%s"%(e))
		# sys.exit()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',## REST
    'bank_d',
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

ROOT_URLCONF = 'ajay_fyle.urls'

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

WSGI_APPLICATION = 'ajay_fyle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE'	: 'django.db.backends.sqlite3',
#         'NAME'	: os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

## MY-SQL Config
# DATABASES = {
#     'default': {
#         'ENGINE'		: 'django.db.backends.mysql', 
#         'NAME'		: 'bank',
#         'USER'		: 'root',
#         'PASSWORD'	: 'toor',
#         'HOST'		: 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT'		: '3306',
#     }
# } 

## Postgresql
DATABASES = {
    'default': {
        'ENGINE'	: 'django.db.backends.postgresql',
        'NAME'		: DB_NAME,                      
        'USER'		: DB_USER_NAME,
        'PASSWORD'	: DB_PASSWORD,
        'HOST'		: DB_HOST,
        'PORT'		: DB_PORT,
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

LANGUAGE_CODE 	= 'en-us'
TIME_ZONE 		= 'UTC'
USE_I18N 		= True
USE_L10N 		= True
USE_TZ 			= True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/ec2-user/static/'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA'			: datetime.timedelta(days=5),
    'JWT_ALLOW_REFRESH'				: True,
    'JWT_REFRESH_EXPIRATION_DELTA'	: datetime.timedelta(days=7),
    'JWT_SECRET_KEY'				: JWT_SECRET_KEY,
}