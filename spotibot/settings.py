# pylint: disable-all

import os
from pathlib import Path
from configparser import ConfigParser


# Config ======================================================================

config = ConfigParser()
config.read("/etc/spotibot/config.ini")


# Settings ====================================================================

ALLOWED_HOSTS = ["*"]
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "%q4mbg=fet*^adhty1q$-bp!9&4+y!9+c)0u*s=_ury*qg#11f"

API_KEY = config["SPOTIBOT"]["API_KEY"]
DEBUG = config["SPOTIBOT"].get("DEBUG", "false") == "true"
LOG_LEVEL = config["SPOTIBOT"].get("LOG_LEVEL", "INFO")
VERSION = config["SPOTIBOT"]["VERSION"]


SPOTIFY = {
    "USERNAME": config["SPOTIFY"]["USERNAME"],
    "CLIENT_ID": config["SPOTIFY"]["CLIENT_ID"],
    "CLIENT_SECRET": config["SPOTIFY"]["CLIENT_SECRET"],
    "PLAYLISTS": {
        "DISCOVER": config["PLAYLISTS"]["DISCOVER"],
        "HISTORY": config["PLAYLISTS"]["HISTORY"],
        "WEEKLIES": {
            "2021": config["PLAYLISTS"]["WEEKLIES_2021"],
        },
    },
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config["DATABASE"]["NAME"],
        "USER": config["DATABASE"]["USER"],
        "PASSWORD": config["DATABASE"]["PASSWORD"],
        "HOST": config["DATABASE"]["HOST"],
        "PORT": int(config["DATABASE"]["PORT"]),
    }
}

SWAGGER_SETTINGS = {
    "DEEP_LINKING": True,
    "DEFAULT_MODEL_RENDERING": "example",
    "DOC_EXPANSION": "none",
    "TAGS_SORTER": "alpha",
    "USE_SESSION_AUTH": False,
}

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
STATIC_ROOT = os.path.join(BASE_DIR, "static")
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

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "MAX_PAGE_SIZE": 50,
}

# Internationalization ========================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIMESTAMPS_TIMEZONE = "Europe/Prague"


# Finish ======================================================================
print(f"Loaded settings {VERSION}")
print(f" * DEBUG = {DEBUG}")
print(f" * LOG_LEVEL = {LOG_LEVEL}")
print(f" * USERNAME = {SPOTIFY['USERNAME']}")
