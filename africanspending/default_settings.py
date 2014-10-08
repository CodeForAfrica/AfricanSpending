import os

DEBUG = not bool(os.environ.get('PROD'))
ASSETS_DEBUG = DEBUG

FLATPAGES_ROOT = '../pages'
FLATPAGES_EXTENSION = '.md'
