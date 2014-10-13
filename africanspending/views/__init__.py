from flask import render_template, redirect, url_for

from africanspending.app import app
from africanspending.views import glossary, page # noqa
from africanspending.views.countries import country # noqa
from africanspending.data import countries


@app.context_processor
def inject_globals():
    return {
        'countries': countries
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<file_name>.txt', methods=['GET'])
def root_txt(file_name):
    # used for robots.txt, humans.txt
    return app.send_static_file('%s.txt' % file_name)


@app.route('/library')
def library_index():
    return redirect(url_for('country_index'))