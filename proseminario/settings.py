"""
Django settings for proseminario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '07@dy_6zz5&j+(&e2g$v#k^m+sdr=i79zl8g#y!4k-!!q4f%@x'

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
    'proseminario.apps.principal',
    'proseminario.apps.usuarios',
    'captcha',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proseminario.urls'

WSGI_APPLICATION = 'proseminario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT':''
    }  
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'proseminario/media')
TEMPLATE_DIRS=(os.path.join(BASE_DIR,'proseminario/templates'),)
STATICFILES_DIRS=(os.path.join(BASE_DIR,'proseminario/static'),)
#Capcha
RECAPTCHA_PUBLIC_KEY = '6LcOTvwSAAAAAMQYA4DpRIL-0z7v4cQXZghF7yp4'
RECAPTCHA_PRIVATE_KEY = '6LcOTvwSAAAAAEu9W75F_mKDpQUwS8dYcuZNXkgs'

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_FACEBOOK_KEY = '1568612763352281'
SOCIAL_AUTH_FACEBOOK_SECRET = '3dd81c64a2942e85637bbe6ea5955694'

LOGIN_URL   ='/login/'
LOGIN_REDIRECT_URL   ='/blog/active/'