from flask import Flask
from config import *
apli = Flask(__name__)
apli.config["SECRET_KEY"] = "sieuj3@Sjwq1"
from app import routes
