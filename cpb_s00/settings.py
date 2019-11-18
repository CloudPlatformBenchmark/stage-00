import os
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = Path(__file__).parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")


# --- Error Reporting ---

if os.getenv("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        environment=os.getenv("SENTRY_ENVIRONMENT"),
        integrations=[DjangoIntegration()],
    )


# --- Basic things ---

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") == "yes"

ALLOWED_HOSTS = ["*"]

BASE_URL = os.getenv("BASE_URL")


# --- Apps ---

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "cpb_s00_api",
]


# --- Global conf ---

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cpb_s00.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ]
        },
    }
]

WSGI_APPLICATION = "cpb_s00.wsgi.application"


# --- Password validation ---

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --- Internationalization ---

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# --- Static files ---

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [BASE_DIR / "cpb_s00" / "static"]

STATICFILES_STORAGE = "cpb_s00.storage.GzipManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"


# --- Emails ---

if os.getenv("ENABLE_EMAILS") != "yes":
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
