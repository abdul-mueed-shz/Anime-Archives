from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'anime-api',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = ['*']
# CORS_ORIGIN_WHITELIST = ('http://localhost:5000',)
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3030',
# ]
