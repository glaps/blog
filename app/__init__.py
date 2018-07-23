import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask
from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
apli = Flask(__name__)
apli.config["SECRET_KEY"] = "sieuj3@Sjwq1"
apli.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
apli.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(apli)
migrate = Migrate(apli, db)
from app import routes, models
