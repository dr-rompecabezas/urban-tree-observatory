import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa: F403
from .base import env, STORAGES

# Docker-specific GeoDjango settings
GDAL_LIBRARY_PATH = env(
    "GDAL_LIBRARY_PATH", default="/usr/lib/aarch64-linux-gnu/libgdal.so.32"
)
GEOS_LIBRARY_PATH = env(
    "GEOS_LIBRARY_PATH", default="/usr/lib/aarch64-linux-gnu/libgeos_c.so.1"
)

# Security settings
DEBUG = False
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS", default=["ibague.gov.co", "www.ibague.gov.co"]
)  # Update with actual domain

# Configure secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configure static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Database configuration - use environment variables
DATABASES = {
    "default": env.db("DATABASE_URL")  # Use the environment variable
}

# S3 Storage for media files in production
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_DEFAULT_ACL = "public-read"
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default="us-east-1")

# Update STORAGES config to use S3
STORAGES = {
    **STORAGES,  # Import base settings
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
}
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Configure Sentry for error monitoring
sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.5,
    send_default_pii=True,
)
