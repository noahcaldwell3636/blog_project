"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.core.management.utils import get_random_secret_key

# Base and template directories
########################################################################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
BASE_TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
BLOG_TEMPLATE_DIR = os.path.join(BASE_DIR,'blog/templates')
# SOCIAL_TEMPLATE_DIR = os.path.join(BASE_DIR, 'social/templates')
# ACCOUNTS_TEMPLATE_DIR = os.path.join(BASE_DIR, 'social/accounts/templates')
# GROUPS_TEMPLATE_DIR = os.path.join(BASE_DIR, 'social/groups/templates')
# POSTS_TEMPLATE_DIR = os.path.join(BASE_DIR, 'social/posts/templates')
########################################################################


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hzetdi)f#0okx$zu5y=7aae$9e6q25#+wmlu%)#=1s9h-m5s&_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "True"

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # NON-DEFAULT INSTALLED APPS 

    # tools for human readable data
    'django.contrib.humanize',  
    # provides dynamic graph functionality
    # 'django_plotly_dash.apps.DjangoPlotlyDashConfig',  
    # styling package use {% load 'bootstrap3' %} to use html/css classes
    'bootstrap3', 
    # tagging for blog post functionality 
    'taggit',
    # command line extensions for managing django projects
    'django_extensions',

    # CREATED APPS

    'blog', # Personal/admin annco
    'social', # contains all of the basic user's functionality
    'social.accounts', # non-admin/basic user accounts
    'social.groups', # reddit-like pages for the users to interact
    'social.posts', # text or media posts for communication
]

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

ROOT_URLCONF = 'mysite.urls'

# designate the locations of the html template folders so the django
# framework can find the html files when referenced in a view
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_TEMPLATE_DIR,
            BLOG_TEMPLATE_DIR,
            # social apps
            # SOCIAL_TEMPLATE_DIR,
            # ACCOUNTS_TEMPLATE_DIR,
            # GROUPS_TEMPLATE_DIR,
            # POSTS_TEMPLATE_DIR,
        ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
# where 'collectstatic' sends all the staic files, not needed until deployment 
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

BASE_STATIC_DIR = os.path.join(BASE_DIR, 'mysite/static')
BLOG_STATIC_DIR = os.path.join(BASE_DIR, 'blog/static')
SOCIAL_STATIC_DIR = os.path.join(BASE_DIR, 'social/static')

STATICFILES_DIRS = [
    ('base', BASE_STATIC_DIR),
    ('blog', BLOG_STATIC_DIR),
    ('social', SOCIAL_STATIC_DIR),
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# allows django to use frames within the html for the dash applications
# X_FRAME_OPTIONS = 'SAMEORIGIN'

# Taggit library 
TAGGIT_CASE_INSENSITIVE = True

# this is the location where the uploaded media from the blog posts is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'blog_media')
MEDIA_URL = '/blog_media/'

