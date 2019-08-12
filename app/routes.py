from app import app, db
from app.models import Blog
from flask import render_template, redirect, url_for, request
from markdown2 import Markdown

context = {
    'blogs': [],
}
md = Markdown()

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
    blog = Blog.query.filter_by(title=title).first_or_404().__dict__
    blog['text'] = md.convert(blog['text'])
    return render_template('blog.html', content=blog, **context)

@app.route('/about')
def about():
    return render_template('about.html', **context)


@app.route('/blog/<title>/edit', METHODS=['GET', "POST"])
def edit_blog(title):
    blog = Blog.query.filter_by(title=title).first()
    if request.method == "GET":
        blog = blog.__dict__ if blog else None
        return render_template('edit.html', content=blog, **context)
    # POST handling
    data = request.get_json()
    if not blog:
        db.session.add(Blog(**data))
    else:
        blog.__dict__.update(data)
    db.session.commit()
    

