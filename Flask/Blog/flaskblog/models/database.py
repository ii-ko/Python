import datetime
from flask_login import UserMixin
from flaskblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.Text, default='default.png')
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    post = db.relationship('Post', backref='author', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)