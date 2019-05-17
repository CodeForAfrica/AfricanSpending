from future import standard_library
standard_library.install_aliases()
import os
import yaml
import unicodecsv
import requests
from io import StringIO
from slugify import slugify

LIB_URL = 'https://docs.google.com/spreadsheets/d/1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos/export?format=csv&id=1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos&gid=200338139'
TOP_URL = 'https://docs.google.com/spreadsheets/d/1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos/export?format=csv&id=1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos&gid=137363156'

my_path = os.path.dirname(__file__)

out = {}


def make_list(val):
    return [o for o in [o.strip() for o in val.split(',')] if len(o)]

for row in unicodecsv.DictReader(StringIO(requests.get(LIB_URL).content)):
    record = {}
    for k, v in list(row.items()):
        k = k.strip().lower()
        v = v.strip()
        if len(v):
            record[k] = v
    if not record.get('slug'):
        record['slug'] = slugify(record.get('label'))
    record['orgs'] = make_list(record.get('orgs', ''))
    record['tags'] = make_list(record.get('tags', ''))
    record['topics'] = make_list(record.get('topics', ''))
    out[record['slug']] = record


with open(os.path.join(my_path, '../data/library/data.yaml'), 'wb') as fd:
    fd.write(yaml.safe_dump(out, canonical=False,
                            default_flow_style=False,
                            allow_unicode=True,
                            indent=2))


out = {}
for row in unicodecsv.DictReader(StringIO(requests.get(TOP_URL).content)):
    record = {}
    for k, v in list(row.items()):
        k = k.strip().lower()
        v = v.strip()
        if len(v):
            record[k] = v
    record['slug'] = slugify(record.get('slug'))
    out[record['slug']] = record


with open(os.path.join(my_path, '../data/library/topics.yaml'), 'wb') as fd:
    fd.write(yaml.safe_dump(out, canonical=False,
                            default_flow_style=False,
                            allow_unicode=True,
                            indent=2))

