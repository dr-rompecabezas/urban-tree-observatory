import os

from django.core.wsgi import get_wsgi_application

# Use development settings by default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_wsgi_application()
