from flask import render_template, redirect, url_for

from africanspending.app import app
from africanspending.views import page # noqa
from africanspending.views.library import country # noqa
from africanspending.data import load_countries, load_library
from africanspending.data import load_topics


@app.context_processor
def inject_globals():
    countries = load_countries()
    map_links = {}
    for k, v in countries.items():
        map_links[v.get('iso3')] = v.get('path')
    return {
        'countries': countries,
        'map_links': map_links,
        'library': load_library(),
        'topics': load_topics()
    }


@app.route('/')
@app.route('/index.html')
def index():
    return redirect(url_for('library'))
    #return render_template('index.html')


@app.route('/<file_name>.txt', methods=['GET'])
def root_txt(file_name):
    # used for robots.txt, humans.txt
    return app.send_static_file('%s.txt' % file_name)
