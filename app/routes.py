from app import app, db
from app.models import Blog
from flask import render_template, redirect, url_for, request

context = {
    'blogs': [],
}

@app.before_request
def refresh_context():
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

@app.route('/about')
def about():
    return render_template('about.html', **context)


@app.route('/blog/<title>/edit', methods=['GET', "POST"])
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
        blog.title = data['title'] if data['title'] != '' else blog.title
        blog.text = data['text'] if data['text'] != '' else blog.text
        db.session.add(blog)
    db.session.commit()
    return 'true'
    

