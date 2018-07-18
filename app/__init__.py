from flask import Flask
from config import Config
apli = Flask(__name__)
apli.config.from_object(Config)
from app import routes
