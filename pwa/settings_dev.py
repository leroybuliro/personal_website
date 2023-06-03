import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('LOST'),
    '127.0.0.1',
    "localhost",
]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False