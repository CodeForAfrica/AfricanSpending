import os
import yaml
from slugify import slugify

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


countries = read_yaml('library/countries')
for key, country in countries.items():
    country['slug'] = slugify(country.get('label'))


