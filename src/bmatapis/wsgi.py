"""
WSGI config for bmatapis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys

sys.path.append('/home/gustavo_visionpura/apps/bmat-tv-av/src')
sys.path.append('/home/gustavo_visionpura/apps/bmat-tv-av/src/bmatapis')
sys.path.append('/home/gustavo_visionpura/apps/bmat-tv-av/env/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmatapis.settings")

application = get_wsgi_application()
