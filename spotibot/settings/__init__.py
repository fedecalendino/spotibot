# pylint: disable-all

import os
from pathlib import Path


# Settings ====================================================================

ALLOWED_HOSTS = ["*"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
SECRET_KEY = "%q4mbg=fet*^adhty1q$-bp!9&4+y!9+c)0u*s=_ury*qg#11f"

API_KEY = "IU48O3IYMra2u6J"

SPOTIFY = {
    "USERNAME": "",
    "CLIENT_ID": "",
    "CLIENT_SECRET": "",
    "PLAYLISTS": {
        "DISCOVER": "",
        "HISTORY": "",
    },
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "spotibot",
        "USER": "spotibot",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

SWAGGER_SETTINGS = {
    "DEEP_LINKING": True,
    "DEFAULT_MODEL_RENDERING": "example",
    "DOC_EXPANSION": "none",
    "TAGS_SORTER": "alpha",
    "USE_SESSION_AUTH": False,
}

LOG_LEVEL = "INFO"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s][%(asctime)s] > %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
        "propagate": False,
    },
    "loggers": {
        "django.server": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        }
    },
}


# Applications ================================================================

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
]

SPOTIBOT_APPS = [
    "spotibot.apps.album",
    "spotibot.apps.artist",
    "spotibot.apps.history",
    "spotibot.apps.job",
    "spotibot.apps.track",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + SPOTIBOT_APPS


# Django ======================================================================

ROOT_URLCONF = "spotibot.urls"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR.parent, "static")
WSGI_APPLICATION = "spotibot.wsgi.application"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Internationalization ========================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIMESTAMPS_TIMEZONE = "Europe/Prague"
