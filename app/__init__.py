from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys  

def init():
    reload(sys)  
    sys.setdefaultencoding('utf8')
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = init()
db = SQLAlchemy(app)

from app import views, models
