from datetime import datetime
from hashlib import md5
from time import time

import bcrypt,jwt
from flask import current_app
from flask_login import UserMixin
from flask_pymongo import ObjectId

from ext import login, mongo
from collections import namedtuple



extraAttr = ['experience', 'award', 'file']
extrabase = namedtuple('extrabase', extraAttr)

projectsAttr = ['pid', 'pname', 'file']
projectsbase = namedtuple('projectsbase', projectsAttr)

userAttr = ['name', 'passwd', 'email', 'path',
            'admin', 'profile', 'projects', 'extra']
userbase = namedtuple('userbase', userAttr)

profileAttr = ['avatar', 'realname',
                   'phonenum', 'college', 'status', 'birth']
profilebase = namedtuple('profilebase', profileAttr)
        

class User(UserMixin):
    
    def __init__(self, name,**args):
        ua = {k: args[k] if k in args.keys() else None for k in userAttr}
        self.name = name
        self.base = userbase(**ua)

    def get_id(self):
        return self.name

    def get_post_num(self):
        if self.base.projects:
            return len(self.base.projects)
        return False

    def get_token(self, expires_in=600):
        return jwt.encode(
            {
                'reset_password': self.name,
                'exp': time() + expires_in
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    # def verify_token(self,token):
    #     bcrypt.hashpw(self.name.encode('utf-8'), bcrypt.gensalt())
    #     return User.query.get(id)

    
    def set_passwd(self):
        users = mongo.db.users
        u = users.find_one({'name': self.name})
        if(u):
            u['passwd'] = bcrypt.hashpw(
                self.base.passwd.encode('utf-8'), bcrypt.gensalt())
            users.save(u)
        else:
            users.insert(**self.base)

    def validate_login(self,passwd):
        passwd_hash = bcrypt.hashpw(passwd.encode('utf-8'), self.base.passwd)
        return passwd_hash == passwd

    @staticmethod
    def verify_token(token):
        try:
            name = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        users = mongo.db.users
        return users.find_one({'name': name})


class Profile(UserMixin):

    def __ini__(self,**args):
        ua = {k: args[k] if k in args.keys() else None for k in profileAttr}
        digest = md5(self.name.lower().encode('utf-8')).hexdigest()
        size = 256
        avatar = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        ua['avatar'] = avatar
        self.base = profilebase(**ua)




@login.user_loader
def load_user(name):
    users = mongo.db.users
    user = users.find_one({'name': name})
    if user:
        return User(name,**user)
    return user
