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
app = init()
login = LoginManager(app)
mongo= PyMongo(app)
login.login_view = 'login'
login.login_message = '请登录后访问'

from app import views, models, errors
