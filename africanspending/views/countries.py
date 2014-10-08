from werkzeug.exceptions import NotFound
from flask import render_template, redirect, url_for

from africanspending.app import app
from africanspending.data import countries


@app.route('/library/countries')
def country_index():
    return render_template('country_index.html')


@app.route('/library/countries/<slug>')
def country(slug):
    if slug in countries:
        slug = countries.get(slug).get('slug')
        return redirect(url_for('country', slug=slug))

    for k, country in countries.items():
        if country['slug'] == slug:
            return render_template('country.html', country=country)
    raise NotFound()
