from werkzeug.exceptions import NotFound
from flask import render_template, url_for

from africanspending.app import app
from africanspending.data import load_countries, load_library


def sort_items(items):
    return sorted(items, key=lambda i: i.get('label'))


@app.route('/library/index.html')
def library():
    return render_template('library.html')


@app.route('/library/organisations/<slug>.html')
def organisation(slug):
    return ''


@app.route('/library/topics/<slug>.html')
def topic(slug):
    return ''


@app.route('/library/countries/<slug>.html')
def country(slug):
    for k, country in load_countries().items():
        if country['slug'] == slug:
            library_items = []
            for slug, item in load_library().items():
                if k in item.get('countries', []):
                    library_items.append(item)
            return render_template('country.html',
                                   country=country,
                                   library_items=sort_items(library_items))
    raise NotFound()
