from distutils.command.build_scripts import first_line_re
import email
from email.policy import default
from re import U
from time import time
from . import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))  
    date=db.Column(db.DateTime(timezone=True),default=db.func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(255),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(255))
    notes=db.relationship('Note')    