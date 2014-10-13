from werkzeug.exceptions import NotFound
from flask import render_template, url_for

from africanspending.app import app
from africanspending.data import load_countries, load_library


def sort_items(items):
    return sorted(items, key=lambda i: i.get('label'))


@app.route('/library/organisations')
def organisation_index():
    return ''


@app.route('/library/organisations/<slug>')
def organisation(slug):
    return ''


@app.route('/library/topics')
def topic_index():
    return ''


@app.route('/library/topics/<slug>')
def topic(slug):
    return ''


@app.route('/library/countries')
def country_index():
    return render_template('country_index.html')


@app.route('/library/countries/<slug>')
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



