from app import app, db
from app.models import Blog, Comment, Admin
from flask import render_template, redirect, url_for, request
from flask_login import login_required

from pprint import pprint

context = {
    'blogs': [],
}

def objToDict(obj):
    return {
        'id': obj.id,
        'username': obj.username,
        'text': obj.text,
        'children': [],
    }

def subComments(clist):
    for c in map(objToDict, clist):
        c['children'].extend(
            subComments(
                Comment.query.filter_by(
                    parent=c['id']
                ).all()
            )
        )
        yield c


@app.before_request
def refresh_context():
    if any(Blog.query.all()):
        context.update({
            'blogs': sorted([x.title for x in Blog.query.all()]),
        })

@app.route('/')
def index():
    return render_template("index.html", **context)

@app.route('/blog/<title>', methods=["GET", "POST"])
def blog(title):
    if request.method == "GET":
        blog = Blog.query.filter_by(title=title).first_or_404()
        comments = list(subComments(Comment.query.filter_by(blog=blog.id).all()))
        print(blog.id)
        print(Comment.query.filter_by(blog=blog.id).all())
        pprint(comments)
        return render_template('blog.html', content=blog, comments=comments, **context)
    else:
        try:
            data = request.get_json()
            c = Comment(**data)
            db.session.add(c)
            db.session.commit()
        except:
            return "False"
        return "True"
        

@app.route('/about')
def about():
    return render_template('about.html', **context)

@login_required
@app.route('/blog/<title>/edit', methods=["GET", "POST"])
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
    

@app.route('/auth', methods=["POST"])
def login():
    data = request.get_json()
    return "false"
