import os
import yaml
import unicodecsv
import requests
from StringIO import StringIO
from slugify import slugify

URL = 'https://docs.google.com/spreadsheets/d/1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos/export?format=csv&id=1o7OM-UL9hbX3fRkGQUcDEFIAHTOmxnu-pQI_2tKFHos&gid=200338139'

my_path = os.path.dirname(__file__)
out_file = os.path.join(my_path, '../data/library/data.yaml')

out = {}

res = requests.get(URL)
fh = StringIO(res.content)


def make_list(val):
    return filter(lambda o: len(o), map(lambda o: o.strip(), val.split(',')))

for row in unicodecsv.DictReader(fh):
    record = {}
    for k, v in row.items():
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


with open(out_file, 'wb') as fd:
    fd.write(yaml.safe_dump(out, canonical=False,
                            default_flow_style=False,
                            allow_unicode=True,
                            indent=2))

