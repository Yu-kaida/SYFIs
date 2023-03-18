from scr import db
from datetime import datetime

class Member(db.Model):
    __tablename__ = 'member'
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    username = db.Column(db.String(80), unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    fav1 = db.relationship('Fav1', backref='member', lazy=True)
    fav2 = db.relationship('Fav2', backref='member', lazy=True)
    fav3 = db.relationship('Fav3', backref='member', lazy=True)
    fav4 = db.relationship('Fav4', backref='member', lazy=True)
    fav5 = db.relationship('Fav5', backref='member', lazy=True)