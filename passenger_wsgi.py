"""
WSGI config for diploDoc diploDoc.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os, sys
sys.path.insert(0, '/home/e/elicta7e/elicta7e.beget.tech/diploDoc')
sys.path.insert(1, '/home/e/elicta7e/elicta7e.beget.tech/vl/lib/python3.10/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'diploDoc.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()