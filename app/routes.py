from app import app, db
from app.models import Blog
from flask import render_template, redirect, url_for

context = {
    'blogs': [],
}

@app.before_request
def refresh_context():
    print("Updating!!")
    context.update({
        'blogs': [x.title for x in Blog.query.all()],
    })

@app.route('/')
def index():
    return render_template("index.html", **context)

@app.route('/blog/<title>')
def blog(title):
    blog = Blog.query.filter_by(title=title).first_or_404()
    return render_template('blog.html', content=blog, **context)
