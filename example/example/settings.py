from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECRET_KEY = "django-seriously-insecure"

DEBUG = True

INSTALLED_APPS = [
    "app",
    "django_migrations_ci",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": BASE_DIR / "dbtest.sqlite3",
        },
    }
}

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
        },
    },
    "loggers": {
        "django_migrations_ci": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

AWS_STORAGE_BUCKET_NAME = "example-migrateci-cache"
AWS_S3_REGION_NAME = "us-east-2"
