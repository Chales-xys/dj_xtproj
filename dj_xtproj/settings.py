"""
Django settings for dj_xtproj project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o6p_en%@a*-t+xw)dcb#tyhs@4@kcd2)=rjy*i0hix+*$dl8qw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#  要写服务器的ip地址
ALLOWED_HOSTS = ["127.0.0.1","39.108.85.200","www.fz66.top"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.cms',
    'apps.news',
    'apps.payinfo',
    'apps.course',
    'apps.xfzauth',
    'apps.ueditor',
]
#AUTH_USER_MODEL:是django内置的，会主动到这个文件来查找这个属性，如果找到了，就会使用这个属性
#指定的模型来作为user对象，AUTH_USER_MODEL：这个属性是一个字符串，他的规则是appname.Modelname
#如果我们设置了AUTH_USER_MODEL，那么项目的迁移必须在以上设置完成之后在执行。
AUTH_USER_MODEL = 'xfzauth.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_xtproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':['django.templatetags.static']#将static标签作为内置标签，不用再每次load
        },
    },
]

WSGI_APPLICATION = 'dj_xtproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'dj_xt',
        'USER':'admin',
        'PASSWORD':'Root110qwe',
        'HOST':'39.108.85.200',
        'port':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR,'/static_dist/')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# ueditor的相关配置,上传至自己服务器的版本
UEDITOR_UPLOAD_TO_SERVER = True
UEDITOR_UPLOAD_PATH = MEDIA_ROOT
UEDITOR_CONFIG_PATH =os.path.join(BASE_DIR,'static','ueditor','config.json') # 读取配置信息

# ueditor 上传至七牛云版本
UEDITOR_QINIU_ACCESS_KEY = ""
UEDITOR_QINIU_SECRET_KEY = ""
UEDITOR_QINIU_BUCKET_NAME = ""
UEDITOR_QINIU_DOMAIN = ""
UEDITOR_UPLOAD_TO_QINIU = True

# 设置新闻首页list每页显示新闻数量
ONE_PAGE_NEWS_COUNT = 1

# 百度云的配置
# 控制台——>用户中心->用户ID
BAIDU_CLOUD_USER_ID = '7d8946c0276f496fb08b0ce6d921a664'
# 点播VOD->全局设置->发布设置->安全设置->UserKey
BAIDU_CLOUD_USER_KEY = '7538c073627c4c0e'