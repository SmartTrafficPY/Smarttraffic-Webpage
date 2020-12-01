import os

from .base import *  # noqa

DEBUG = os.getenv('DJANGO_DEBUG', False)
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
