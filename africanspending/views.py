from flask import render_template

from africanspending.app import pages, app
from africanspending.glossary import by_slug


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<file_name>.txt', methods=['GET'])
def root_txt(file_name):
    # used for robots.txt, humans.txt
    return app.send_static_file('%s.txt' % file_name)


@app.route('/pages/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'pages.html')
    return render_template(template, page=page)


@app.route('/glossary/<slug>')
def glossary(slug):
    data = by_slug(slug)
    # todo: 404
    # todo: render
    return unicode(data)
