import os
import yaml
from slugify import slugify

from africanspending.app import app


def read_glossary():
    with open(os.path.join(app.data_path, 'glossary.yaml'), 'r') as fh:
        entries = yaml.load(fh)

    for entry in entries:
        entry['slug'] = slugify(entry.get('term'))
    
    return entries


def by_slug(slug):
    for entry in read_glossary():
        if entry['slug'] == slug:
            return entry
