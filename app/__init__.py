import sys  
import os
from flask_login import LoginManager
from config import basedir
from flask import Flask
from flask_pymongo import PyMongo

def init():
    # reload(sys)  
    # sys.setdefaultencoding('utf8')
    app = Flask(__name__)
    app.config.from_object('config')
    return app
lm = LoginManager()
app = init()
lm.init_app(app)
mongo= PyMongo(app)

from app import views
