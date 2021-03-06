

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$(tba4%d8_xev2=8&6)gs0#og3&q89q^))eg7kw6ulex96@!^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'certification.apps.CertificationConfig',
    'accounts.apps.AccountsConfig',#ユーザー認証

    'django.contrib.sites',#for djnago-allauth
    'allauth',#for djnago-allauth
    'allauth.account',#for djnago-allauth
    'allauth.socialaccount',#for djnago-allauth
    'customer.apps.CustomerConfig',
    'qrfunction.apps.QrfunctionConfig',
    'CustomerAccounts.apps.CustomeraccountsConfig', #利用者の認証一式

    'routing.apps.RoutingConfig',
    'widget_tweaks',#django-form用

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.backends.signed_cookies',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

MIDDLEWARE_CLASSES = [
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#staticのcssが反映される
STATICFILES_DIRS =(
    os.path.join(BASE_DIR, 'static'),
)

AUTH_USER_MODEL = 'accounts.CustomUser'

#追加
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 認証方式を「ユーザーネーム（施設名）」に変更
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ユーザー名を使用する
ACCOUNT_USERNAME_REQUIRED = True

# ユーザー登録確認メールは送信しない
ACCOUNT_EMAIL_VERIFICATION = 'none'
# メールアドレスを必須項目にする
ACCOUNT_EMAIL_REQUIRED = False

#ユーザーモデルの拡張(customuser)
AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1 #django-allauthがsitesフレームワークを使っているため

LOGIN_REDIRECT_URL = 'certification:facility'
ACCOUNT_LOGOUT_REDIRECT_URL = 'certification:facility'
ACCOUNT_LOGOUT_ON_GET = True

#signupformを指定
ACCOUNT_FORMS = {
    'signup' : 'accounts.forms.CustomSignupForm',
    'login' : 'accounts.forms.CustomLoginForm',
}
#signupformからの情報をcustomusermodelに保存するのに必要
ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'

#passwordの入力を一回に
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False