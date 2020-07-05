from app import db, login_manager
from datetime import datetime
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

"""
SubTable = db.Table('subtable',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('match_id', db.Integer, db.ForeignKey('matches.id'), primary_key=True))
"""

class User(db.Model, UserMixin):
    #set the table name
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    email = db.Column(db.String(32), unique=True, index=True)
    pass_hash = db.Column(db.Text)

#    def __init__(self, name, email, password):
#        
#        self.name = name
#        self.email = email
#        self.pass_hash = generate_password_hash(password)

#    def check_password(self, password):
#        check_password_hash(self.pass_has, password)

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    team_a = db.Column(db.String(10), nullable=False)
    team_b = db.Column(db.String(10), nullable=False)
    venue = db.Column(db.String(10))
    #result = db.Column(db.String(50))

    #Below realtionship doesnt work, it will create same data for both for_team_a and for_team_b
    #for_team_a = db.relationship('User', secondary=SubTable, backref=db.backref('team_a', lazy=True))
    #for_team_b = db.relationship('User', secondary=SubTable, backref=db.backref('team_b', lazy=True)) 

