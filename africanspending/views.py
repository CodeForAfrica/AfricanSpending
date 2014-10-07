from flask import render_template

from africanspending.app import pages, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<file_name>.txt', methods=['GET'])
def root_txt(file_name):
    # used for robots.txt, humans.txt
    return app.send_static_file('%s.txt' % file_name)


@app.route('/pages/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'pages.html')
    return render_template(template, page=page)
