from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Use in-memory SQLite for tests to speed up
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
