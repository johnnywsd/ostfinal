"""

Django settings for final project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')fa-bom7cj42smv!95pk0l@3)$4&jrarcz%i^1=b!4=*m%zp+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'south',
    'pagination_bootstrap',
    'ckeditor',
    'django.contrib.sites',
    #'django_comments',
    'django.contrib.comments',
    'django_comments_xtd',
    #'tracking',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'final.urls'

WSGI_APPLICATION = 'final.wsgi.application'


#COMMENT
COMMENTS_APP = "django_comments_xtd"
#COMMENTS_APP = "django_comments"
COMMENTS_XTD_CONFIRM_EMAIL = False
COMMENTS_XTD_MAX_THREAD_LEVEL = 3
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ostfinal',
        'USER': 'root',
        'PASSWORD': 'wsd19890518',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/mystatic/ostfinal/static'
MEDIA_ROOT = '/var/www/mystatic/ostfinal/media'

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "static"),
)

#django-ckeditor
#CKEDITOR_UPLOAD_PATH = "/home/johnny/tmp/OST/" #Local
CKEDITOR_UPLOAD_PATH = "imgs/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 600,
    },
}
CKEDITOR_IMAGE_BACKEND = "pillow"
MEDIA_CACHE_BUSTER = '_cached'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
TEMPLATE_DIRS=( 
        os.path.join(BASE_DIR,'template'),
        )

#from django.core.urlresolvers import reverse
ROOT_URL=''
#LOGIN_URL= ROOT_URL + reverse('login')
LOGIN_URL= ROOT_URL + 'login'

DATE_FORMAT = '%Y-%m-%d'

#django-storages
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIF7WGEZSJFZIEAFQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'ostfinal'
AWS_QUERYSTRING_AUTH = False

IS_LOCAL = False
if IS_LOCAL:
    try:
        from local_settings import *
    except:
        print 'No Local Settings Found'
