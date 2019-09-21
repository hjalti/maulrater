from .settings import *
import os

SECRET_KEY = 'jrn7*bs+5!^u4g(cxp)ui=$mc$dq9b#t%4)-gi*k!gxka8$%sn'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['*']

DEBUG=False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
