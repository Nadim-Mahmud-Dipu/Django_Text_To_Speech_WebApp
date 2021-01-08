"""
WSGI config for Django_Paper_Text_To_Mp3_Converter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Paper_Text_To_Mp3_Converter.settings')

application = get_wsgi_application()
