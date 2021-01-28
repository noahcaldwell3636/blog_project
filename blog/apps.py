# BLOG - APPS.PY
'''
Creates configuartion objects that store metadata for the application. 
'''
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog' # defines what app the config applies to

