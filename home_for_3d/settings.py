from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 
    '+b$r#%&hiqdyn6z3w-0mz2mvufgpwonxu7760%@2g2ap&&!q0(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
                 'localhost',
                 '.herokuapp.com'
                 ]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-drsyakovlev-homeforaddi-abht9tq6lv8.ws-eu114.gitpod.io',
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'prop_for_3d',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/proposals'
LOGOUT_REDIRECT_URL = '/'

# Django Allauth settings
ACCOUNT_LOGOUT_REDIRECT_URL = (
    '/accounts/login/')  # Redirect to login after logout
ACCOUNT_EMAIL_REQUIRED = True  # Makes email required in sign-up form
ACCOUNT_AUTHENTICATION_METHOD = (
    'username_email')  # Allows users to log in using username or email
ACCOUNT_SIGNUP_REDIRECT_URL = (
    '/proposals')  # Where to redirect after successful sign-up (optional)


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'home_for_3d.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'home_for_3d.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
"""
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com"
]
"""

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# Define the password validators as variables
user_attr_validator = (
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
)
min_length_validator = (
    'django.contrib.auth.password_validation.MinimumLengthValidator'
)
common_password_validator = (
    'django.contrib.auth.password_validation.CommonPasswordValidator'
)
numeric_password_validator = (
    'django.contrib.auth.password_validation.NumericPasswordValidator'
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': user_attr_validator},
    {'NAME': min_length_validator},
    {'NAME': common_password_validator},
    {'NAME': numeric_password_validator},
]


ACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
"""
ACCOUNT_EMAIL_REQUIRED = True  # Makes email required in Allauth
ACCOUNT_UNIQUE_EMAIL = True    # Ensures each email is unique


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
