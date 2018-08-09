import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from config import Config
from flask import Flask
#from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import request




apli = Flask(__name__)
bootstrap = Bootstrap(apli)
moment = Moment(apli)
apli.config.from_object(Config)
mail = Mail(apli)
db = SQLAlchemy(apli)
migrate = Migrate(apli, db)
login = LoginManager(apli)
login.login_view = 'login'

if not apli.debug:
    if apli.config['MAIL_SERVER']:
        auth = None
        if apli.config['MAIL_USERNAME'] or apli.config['MAIL_PASSWORD']:
            auth = (apli.config['MAIL_USERNAME'], apli.config['MAIL_PASSWORD'])
        secure = None
        if apli.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(apli.config['MAIL_SERVER'], apli.config['MAIL_PORT']),
            fromaddr='no-reply@' + apli.config['MAIL_SERVER'],
            toaddrs=apli.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        apli.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    apli.logger.addHandler(file_handler)

    apli.logger.setLevel(logging.INFO)
    apli.logger.info('Microblog startup')




from app import routes, models, errors
