from .base import *

# =====================
# Core Security Settings
# =====================
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# =====================
# Database (PostgreSQL)
# =====================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST", default="db"),
        "PORT": env.str("DB_PORT", default="5432"),
    }
}

# =====================
# HTTPS & Cookie Security
# =====================
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# =====================
# CORS & CSRF Settings
# =====================
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[])

# =====================
# Static & Media Files (for production)
# =====================
STATIC_URL = '/static/'
STATIC_ROOT = env.str('STATIC_ROOT', default='/var/www/static/')  # For Nginx/Apache
MEDIA_URL = '/media/'
MEDIA_ROOT = env.str('MEDIA_ROOT', default='/var/www/media/')

# =====================
# Logging (Critical for Debugging when DEBUG=False)
# =====================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
