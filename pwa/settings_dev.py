import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('LOST'),
]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False