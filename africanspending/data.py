import os
import yaml
from slugify import slugify

from flask import url_for

from africanspending.app import app


def read_yaml(name):
    with open(os.path.join(app.data_path, '%s.yaml' % name), 'r') as fh:
        return yaml.load(fh)


def read_glossary():
    entries = read_yaml('glossary')
    for entry in entries:
        entry['slug'] = slugify(entry.get('term'))
    return entries


def lemma_by_slug(slug):
    for entry in read_glossary():
        if entry['slug'] == slug:
            return entry


def load_countries():
    countries = read_yaml('library/countries')
    for key, country in countries.items():
        country['slug'] = slugify(country.get('label'))
        country['path'] = url_for('country', slug=country['slug'])
        country['key'] = key
    return countries


def load_library():
    library = read_yaml('library/data')
    for slug, item in library.items():
        if item.get('type') == 'organisation':
            item['path'] = url_for('organisation', slug=slug)
    return library


def load_topics():
    topics = read_yaml('library/topics')
    for slug, topic in topics.items():
        topic['path'] = url_for('topic', slug=slug)
    return topics
