"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

import environ
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(env("DEBUG", default=0))

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

DOMAIN = env("DOMAIN")

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ["Authorization", "Content-Type", "Accept"]

if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'unfold',
    "unfold.contrib.forms",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'django_filters',
    'djoser',
    'corsheaders',
    'ckeditor',

    'specialties',
    'news',
    'events',
    'staff',
    'reviews',
    'document_pages',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'djangorestframework_camel_case.middleware.CamelCaseMiddleWare',
    'config.middleware.LanguageMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',   # Используется PostgreSQL
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [f"https://{DOMAIN}", f"http://{DOMAIN}"]

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('ky', 'Kyrgyz'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru', 'en', 'ky')
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': ('ru',),
    'en': ('ru', 'ky'),  # Для английского fallback на русский и кыргызский
    'ky': ('ru',),  # Для кыргызского fallback на русский
}
MODELTRANSLATION_AUTO_POPULATE = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587

SPECTACULAR_SETTINGS = {
    'TITLE': 'Comtehno Backend',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CAMELIZE_NAMES': True,

    'POSTPROCESSING_HOOKS': [
        'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields',
    ],
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Bearer",),
    'UPDATE_LAST_LOGIN': True,
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': False,
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    # 'SERIALIZERS': {
    #     'user': 'account.serializers.UserSerializer',
    #     'current_user': 'account.serializers.UserSerializer',
    # },
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

UNFOLD = {
    "SITE_TITLE": 'Comtehno',
    "SITE_HEADER": "Comtehno",
    "SITE_URL": "/",
    "SITE_SYMBOL": "menu",  # symbol from icon set
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    "BORDER_RADIUS": "6px",
    "COLORS": {
        "base": {
            "50": "249 250 251",
            "100": "243 244 246",
            "200": "229 231 235",
            "300": "209 213 219",
            "400": "156 163 175",
            "500": "107 114 128",
            "600": "75 85 99",
            "700": "55 65 81",
            "800": "31 41 55",
            "900": "17 24 39",
            "950": "3 7 18",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "ru": "ru",
                "en": "en",
                "ky": "ky",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Специальности"),
                "items": [
                    {
                        "title": _("Специальности"),
                        "icon": "school",
                        "link": reverse_lazy("admin:specialties_specialty_changelist"),
                    },
                    {
                        "title": _("Категории специальности"),
                        "icon": "category",
                        "link": reverse_lazy("admin:specialties_specialtycategory_changelist"),
                    },
                    {
                        "title": _("Программа обучения"),
                        "icon": "import_contacts",
                        "link": reverse_lazy("admin:specialties_trainingprogram_changelist"),
                    },
                    {
                        "title": _("Программа обучения - Курсы"),
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:specialties_course_changelist"),
                    },
                    {
                        "title": _("Проекты студентов"),
                        "icon": "developer_board",
                        "link": reverse_lazy("admin:specialties_studentproject_changelist"),
                    },
                    {
                        "title": _("Резюме"),
                        "icon": "sensor_occupied",
                        "link": reverse_lazy("admin:specialties_cv_changelist"),
                    },
                    {
                        "title": _("Инструменты"),
                        "icon": "home_repair_service",
                        "link": reverse_lazy("admin:specialties_tool_changelist"),
                    },
                    {
                        "title": _("Навыки"),
                        "icon": "skateboarding",
                        "link": reverse_lazy("admin:specialties_skill_changelist"),
                    },
                ],
            },
            {
                "title": _("Отзывы"),
                "items": [
                    {
                        "title": _("Отзывы Студенты"),
                        "icon": "person",
                        "link": reverse_lazy("admin:reviews_studentreview_changelist"),
                    },
                    {
                        "title": _("Категории"),
                        "icon": "category",
                        "link": reverse_lazy("admin:reviews_category_changelist"),
                    },
                ],
            },
            {
                "title": _("Новости"),
                "items": [
                    {
                        "title": _("Посты"),
                        "icon": "post",
                        "link": reverse_lazy("admin:news_post_changelist"),
                    },
                    {
                        "title": _("Категории постов"),
                        "icon": "category",
                        "link": reverse_lazy("admin:news_postcategory_changelist"),
                    },
                ],
            },
            {
                "title": _("Мероприятия"),
                "items": [
                    {
                        "title": _("Мероприятие"),
                        "icon": "event",
                        "link": reverse_lazy("admin:events_event_changelist"),
                    },
                    {
                        "title": _("Категории Мероприятия"),
                        "icon": "category",
                        "link": reverse_lazy("admin:events_eventcategory_changelist"),
                    },
                ],
            },
            {
                "title": _("Персонал"),
                "items": [
                    {
                        "title": _("Преподаватели"),
                        "icon": "self_improvement",
                        "link": reverse_lazy("admin:staff_staff_changelist"),
                    },
                    {
                        "title": _("Отделения"),
                        "icon": "account_balance",
                        "link": reverse_lazy("admin:staff_staffdepartment_changelist"),
                    },
                ],
            },
            {
                "title": _("Документы"),
                "items": [
                    {
                        "title": _("Документ страницы"),
                        "icon": "description",
                        "link": reverse_lazy("admin:document_pages_documentpage_changelist"),
                    },
                    {
                        "title": _("Коллекции документов"),
                        "icon": "collections",
                        "link": reverse_lazy("admin:document_pages_documentcollection_changelist"),
                    },
                ],
            },
            {
                "title": _("Проекты и стартапы"),
                "items": [
                    {
                        "title": _("Проекты"),
                        "icon": "preview",
                        "link": reverse_lazy("admin:projects_project_changelist"),
                    },
                ],
            },
            {
                "title": _("Пользователи & Группы"),
                "items": [
                    {
                        "title": _("Пользователи"),
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Группы"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                        # "permission": "account.utils.permission_callback",
                    },
                ],
            },
        ],
    },
}
