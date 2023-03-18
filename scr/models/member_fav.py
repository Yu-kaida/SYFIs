from scr import db

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    fav1 = db.Column(db.String(80), unique=True, nullable=False)
    fav2 = db.Column(db.String(80), unique=True, nullable=False)
    fav3 = db.Column(db.String(80), unique=True, nullable=False)
    fav4 = db.Column(db.String(80), unique=True, nullable=False)
    fav5 = db.Column(db.String(80), unique=True, nullable=False)