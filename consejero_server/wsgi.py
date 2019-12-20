"""
WSGI config for consejero_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'consejero_server.settings'
#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "consejero_server.settings")

#application = get_wsgi_application()

#import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


#application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
application = WhiteNoise(applicatio, root=BASE_DIR+'/static')
application.add_files(BASE_DIR + '/media' , prefix='media/')
