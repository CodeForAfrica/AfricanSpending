import os
from flask import Flask
from flask.ext.assets import Environment
from flask_flatpages import FlatPages

from africanspending import default_settings

app = Flask(__name__)
app.config.from_object(default_settings)
app.config.from_envvar('AS_SETTINGS', silent=True)

assets = Environment(app)
pages = FlatPages(app)

app.data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                '..', 'data'))

if not app.debug:
    assets.auto_build = False
