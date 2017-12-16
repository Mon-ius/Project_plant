from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys  
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir


def init():
    reload(sys)  
    sys.setdefaultencoding('utf8')
    app = Flask(__name__)
    app.config.from_object('config')
    return app
lm = LoginManager()
app = init()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
db = SQLAlchemy(app)

from app import views, models
