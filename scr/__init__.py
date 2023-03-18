from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('scr.config')

db = SQLAlchemy(app)
from .models import member_fav

import scr.views

# To create database
# from scr import app, db
# with app.app_context():
#     db.create_all()