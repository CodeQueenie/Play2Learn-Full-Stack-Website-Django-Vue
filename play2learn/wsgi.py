"""
WSGI config for play2learn project.

It exposes the WSGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Get the WSGI application
application = get_wsgi_application()

# Wrap the WSGI application with WhiteNoise for static file serving
application = WhiteNoise(application)

# Update the DJANGO_SETTINGS_MODULE to match your project's settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "play2learn.settings")