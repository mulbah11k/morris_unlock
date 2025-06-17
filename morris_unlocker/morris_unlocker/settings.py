from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
DEBUG = 'False'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-fallback-secret')

# ALLOWED_HOSTS = [    
#     'morrisunlock-production.up.railway.app', 
#     'localhost',
#     '127.0.0.1',]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'services',
    'orders',
    'wallet',
    'theme',
    'tailwind',
    'adminpanel',
    'whitenoise.runserver_nostatic',
]

if DEBUG:
    INSTALLED_APPS.append('django_browser_reload')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# if DEBUG:
#     MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

TAILWIND_APP_NAME = 'theme'

ROOT_URLCONF = 'morris_unlocker.morris_unlocker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'morris_unlocker.wsgi.application'
DATABASES = {
    'default': dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.CustomUser'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

NPM_BIN_PATH = "/home/mulbahkolleh/.nvm/versions/node/v22.14.0/bin/npm"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
