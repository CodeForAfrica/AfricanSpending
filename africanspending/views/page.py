from flask import render_template

from africanspending.app import app, pages


@app.route('/pages/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'pages.html')
    return render_template(template, page=page)
