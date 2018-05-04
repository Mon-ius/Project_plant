import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
basedir = os.path.join(basedir, 'app')
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'laochenSVIP'
    WTF_CSRF_SECRET_KEY = 'laochenVSVIP'
    UPLOADED_DATA_DEST = os.path.join(basedir, 'uploads')


    MONGO_DBNAME = 'plant'
    MONGO_URI = 'mongodb://CKCHEN:secret@ds259897.mlab.com:59897/plant'
    POSTS_PER_PAGE = 3
    
    ADMINS = os.environ.get('ADMINS')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    #print SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO
