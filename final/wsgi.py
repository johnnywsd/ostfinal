"""
WSGI config for final project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
#import sys
#import site
#import logging
#import django

#logging.error(django.get_version())

# Add the site-packages of the chosen virtualenv to work with
#site.addsitedir('/home/johnny/workspace/Envs/ostfinal/local/lib/python2.7/site-packages ')

# Add the app's directory to the PYTHONPATH
#sys.path.append('/home/johnny/workspace/python/OST/final')
#sys.path.append('/home/johnny/workspace/python/OST/final/final')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

# Activate your virtual env
#activate_env=os.path.expanduser("/home/johnny/workspace/Envs/ostfinal/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


