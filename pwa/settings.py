import socket
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
    
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('pwakey')

if socket.gethostname() == "green-liveconsole11":
    from pwa.settings_prod import *
else:
    from pwa.settings_dev import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'core',
    # 'store',
    
    # Addons
    'ckeditor', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pwa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
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

WSGI_APPLICATION = 'pwa.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.getenv('MYSQLname'),
        'USER': os.getenv('MYSQLuser'),
        'PASSWORD': os.getenv('MYSQLpwd'),
        'HOST': os.getenv('MYSQLhost'),
        'PORT': os.getenv('MYSQLport'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'account.User'
LOGIN_URL = '/account/auth/'
LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static_cdn'), ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')

# AmazonS3 configurations
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# AWS_S3_SESSION_PROFILE = os.getenv('')
# AWS_ACCESS_KEY_ID = os.getenv('')
# AWS_SECRET_ACCESS_KEY = os.getenv('')
# AWS_STORAGE_BUCKET_NAME = os.getenv('')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'full_editor': {
        'toolbar': 'full',
    },
    'custom_editor': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
}

# SMPT Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('PWAEmailUser')
EMAIL_HOST_PASSWORD = os.getenv('PWAEmailPwd')
