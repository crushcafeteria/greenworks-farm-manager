from pathlib import Path
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'manager.apps.ManagerConfig',
    'weather.apps.WeatherConfig',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'crispy_forms',
    "crispy_bootstrap5",
    "debug_toolbar",
    'corsheaders',
    'django_q',
    'django.contrib.humanize'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'greenworks.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'greenworks.context_processors.app_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'greenworks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : env('DB_NAME'),
        'HOST'    : env('DB_HOST'),
        'PORT'    : env('DB_PORT'),
        'USER'    : env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-ke'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

APP_NAME = 'Greenworks'
APP_NAME_FOOTER = 'Greenworks Farm Manager'

CORS_ALLOW_ALL_ORIGINS = True

WEATHER_ENDPOINT = 'http://dataservice.accuweather.com'
WEATHER_API_KEY = '4ooYPXjMeUcoKhzJ0MfaRtzHFqNtXeWx'
LOCATION_KEY = '226539'

Q_CLUSTER = {
    'name'      : 'DjangoORM',
    'timeout'   : 1200,  # Timeout in secs for a task
    'save_limit': 10,  # Store latest 10 results only
    'catch_up'  : False,  # Ignore un-run scheduled tasks
    'orm'       : 'default'  # Django database connection
}
