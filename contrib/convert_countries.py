import yaml
import unicodecsv

COUNTRIES = ['za', 'dz', 'ao', 'bz', 'bw', 'bf', 'bi',
             'cm', 'cf', 'td', 'cg', 'cd', 'dj', 'eg',
             'er', 'et', 'ga', 'gm', 'gh', 'gn', 'gw',
             'ci', 'ke', 'ly', 'ls', 'lr', 'mg', 'mw',
             'ml', 'ma', 'mz', 'na', 'ne', 'ng', 'sn',
             'sl', 'so', 'sd', 'sz', 'tz', 'tn', 'ug',
             'zm', 'zw', 'gq', 'ss', 'bj', 'cv', 'mr',
             'mu', 'rw', 'st', 'sc', 'eh', 'tg']

print len(set(COUNTRIES))

out_file = '../data/library/countries.yaml'

try:
    out = yaml.load(open(out_file, 'rb').read())
except Exception, e:
    print e
    out = {}

with open('countries.csv', 'r') as fh:
    reader = unicodecsv.DictReader(fh)
    for row in reader:
        if row.get('linked_country'):
            continue
        key = row.get('iso2').lower()
        if key not in COUNTRIES:
            continue
        data = {
            'iso2': row.get('iso2'),
            'iso3': row.get('iso3'),
            'label_full': row.get('country'),
            'label': row.get('country'),
        }
        od = out.get(key, {})
        for k, v in data.items():
            if k not in od:
                od[k] = v
        out[key] = od


print 'missing', set(COUNTRIES) - set(out.keys())


with open(out_file, 'wb') as fd:
    fd.write(yaml.safe_dump(out, canonical=False,
                            default_flow_style=False,
                            allow_unicode=True,
                            indent=2))

