# -*- coding: utf-8 -*-
import os, sys
sys.path.append('/home/r/roosevelt/keklol.ru/e-commerce')
sys.path.append('./env/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'db_tutorial.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
