from werkzeug.exceptions import NotFound
from flask import render_template

from africanspending.app import app
from africanspending.data import lemma_by_slug


@app.route('/glossary/<slug>')
def glossary_lemma(slug):
    data = lemma_by_slug(slug)
    if data is None:
        raise NotFound()
    return render_template('glossary_lemma.html', lemma=data)
