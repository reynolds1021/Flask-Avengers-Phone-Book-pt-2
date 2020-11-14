import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\codingtemple-sept2020\week5\day1\intro_to_flask\
# Mac = Mac = Documents/codingtemple-sept2020/week5/day1/introtoflask/

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY') #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
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')