from flask import Flask
from flask.ext.assets import Environment
from flask_flatpages import FlatPages

from africanspending import default_settings

app = Flask(__name__)
app.config.from_object(default_settings)
app.config.from_envvar('AS_SETTINGS', silent=True)

assets = Environment(app)
pages = FlatPages(app)
