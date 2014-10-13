from flask import render_template

from africanspending.app import app
from africanspending.views import page # noqa
from africanspending.views.library import country # noqa
from africanspending.data import load_countries, load_library
from africanspending.data import load_topics


@app.context_processor
def inject_globals():
    return {
        'countries': load_countries(),
        'library': load_library(),
        'topics': load_topics()
    }


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/<file_name>.txt', methods=['GET'])
def root_txt(file_name):
    # used for robots.txt, humans.txt
    return app.send_static_file('%s.txt' % file_name)
