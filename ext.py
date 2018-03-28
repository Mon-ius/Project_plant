from flask_moment import Moment
from flask_mail import Mail, Message
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_babel import Babel, _, lazy_gettext as _l
from datetime import datetime, timedelta
from config import Config

mongo = PyMongo()

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
login.remember_cookie_duration = timedelta(days=30)

mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()