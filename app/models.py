from app import db, login
from sqlalchemy.sql import func
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    """User loader for flask login."""
    return Admin.query.get(int(id))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Blog | title: {self.title}>"


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), nullable=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """Runs the passwords through a hash and appends."""
        self.password_hash = generate_password_hash(str(password))

    def check_password(self, password):
        """Checks a password against the hash."""
        return check_password_hash(self.password_hash, password)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    username = db.Column(db.String(64), index=True, default="anon")
    text = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    blog = db.Column(db.Integer, db.ForeignKey('blog.id'))
    parent = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    rel = db.relationship("Comment", backref="comment", lazy="dynamic")
    rel = db.relationship("Blog", backref="comment")

    def __repr__(self):
        return f"<Comment | User: {self.username}>"