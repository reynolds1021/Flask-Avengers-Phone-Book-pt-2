from flask import Flask

from config import Config

#Import for FLask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Import for Flask Login
from flask_login import LoginManager 

#Import for FLask Mail
from flask_mail import Mail, Message

#Creat Instance of Flask class, name it app 
app = Flask(__name__)
#Add configurations
app.config.from_object(Config)

#Create db and migrator 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login' #Specify what page to load for NON-authenticated users

mail = Mail(app)

from app import routes, models 