import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
MONGO_DBNAME = 'plant'
MONGO_URI = 'mongodb://CKCHEN:secret@ds259897.mlab.com:59897/plant'

CSRF_ENABLED = True
SECRET_KEY = 'laochenSVIP'
#print SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO
