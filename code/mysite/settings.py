#coding=utf-8

import os
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *

#==============================================================================
# Generic Django project settings
#==============================================================================
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# 开发环境的配置
RUN_MODE = 'DEVELOP'
from settings_global_dev import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e#_n#(c1#9x-16o6ajfo1@i(s*7pp4d)3n#b(-r(xq5f2rq*9t'
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-CN'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

#==============================================================================
# Calculation of directories relative to the module location
#==============================================================================
import sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(PROJECT_ROOT)
PYTHON_BIN = os.path.dirname(sys.executable)
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
MEDIA_URL = '/media/' 
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ROOT_URLCONF = 'urls'

#==============================================================================
# file upload handlers
#==============================================================================
FILE_UPLOAD_HANDLERS = (
                       "django.core.files.uploadhandler.MemoryFileUploadHandler",
                       "django.core.files.uploadhandler.TemporaryFileUploadHandler",
                       )

#==============================================================================
# Templates
#==============================================================================
TEMPLATE_CONTEXT_PROCESSORS = (
    # the context to the templates
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'common.context_processors.mysetting',      # 自定义模版context，可以在页面中使用STATIC_URL等变量
    'django.core.context_processors.i18n',
)
# django template dir
TEMPLATE_DIRS = (
    # 绝对路径，比如"/home/html/django_templates" or "C:/www/django/templates".
    os.path.join(PROJECT_ROOT, 'templates'),
)
# mako template dir
MAKO_TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'templates')
MAKO_TEMPLATE_MODULE_DIR = os.path.join(PROJECT_DIR, 'templates_module')


#==============================================================================
# Middleware and apps
#==============================================================================
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django_websocket.middleware.WebSocketMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # OTHER 3rd Party App
    'south',
    # login & logout module
    'passport',
    # add your app here...
    # Note: 请注意在第一次syncdb时只加入south, 而不加自己的app，先syncdb初始化south的数据，
    # 然后再加入自己的app进行south操作!
    'home'
)

#===============================================================================
# websocket config
#===============================================================================
WEBSOCKET_ACCEPT_ALL = True

#===============================================================================
# authentication module settings
#===============================================================================
LOGIN_URL = '/passport/login/'
LOGOUT_URL = '/passport/logout/'
LOGIN_REDIRECT_URL = '/'               # Redirect to home page after login

# store additional infomation about user
AUTH_PROFILE_MODULE = 'passport.UserProfile'

#==============================================================================
# logging
#==============================================================================
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
LOGGING_DIR = os.path.join(PROJECT_DIR, 'logs')

# south log
SOUTH_LOGGING_ON = True
SOUTH_LOGGING_FILE = os.path.join(LOGGING_DIR, 'south.log')

# 自动建立这个目录
if not os.path.exists(LOGGING_DIR):
    try:
        os.makedirs(LOGGING_DIR)
    except:
        pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(pathname)s %(lineno)d %(funcName)s %(process)d %(thread)d \n \t %(message)s \n',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s \n'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'root': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, 'site.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },

    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        # the root logger ,用于整个project的logger
        'root': {
            'handlers': ['root'],
            'level': 'ERROR',
            'propagate': True,
        },
        # other loggers...

    }
}

