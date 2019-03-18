from restaurant_api.settings.settings import *

DJANGO_SETTINGS_MODULE = 'restaurant_api.settings.development'

SECRET_KEY = 'ekdcyo6fsxeheiqqax+net8!o1agxtf82du+29o3@(o_a8ps=2'
DEBUG = True
IS_PRODUCTION = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'restaurant-api',
        'USER': 'postgres',
        'PASSWORD': 'marc'
    }
}
