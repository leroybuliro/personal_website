import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
    
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('pwakey')
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [
    os.environ.get('IPlocal'),
    'buliro.net',
    'www.buliro.net',
    'leroybuliro.pythonanywhere.com',
]

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
        'NAME': os.environ.get('MYSQLname'),
        'USER': os.environ.get('MYSQLuser'),
        'PASSWORD': os.environ.get('MYSQLpwd'),
        'HOST': os.environ.get('MYSQLhost'),
        'PORT': os.environ.get('MYSQLport'),
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

CSRF_COOKIE_AGE = 15724800 #6months
CSRF_COOKIE_SECURE = True
# CSRF_FAILURE_VIEW = 'core.errorviews.csrf_failure'

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_SECONDS = 7200 #2hrs
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_TIMEOUT_REDIRECT = "/"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static_cdn'), ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')

# AmazonS3 configurations
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# AWS_S3_SESSION_PROFILE = os.environ.get('')
# AWS_ACCESS_KEY_ID = os.environ.get('')
# AWS_SECRET_ACCESS_KEY = os.environ.get('')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('')

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
EMAIL_HOST_USER = os.environ.get('PWAEmailUser')
EMAIL_HOST_PASSWORD = os.environ.get('PWAEmailPwd')
