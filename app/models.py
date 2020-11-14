from app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False, unique=True)
    lastname = db.Column(db.String(100), nullable=False, unique=True)
    heroname = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False, unique=True)
    phonenumber = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, firstname, lastname, heroname, address, phonenumber, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.heroname = heroname 
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        pw_hash = generate_password_hash(password)
        return pw_hash     

    def __repr__(self):
        return  f"<Hero | {self.hero_name}>"   
