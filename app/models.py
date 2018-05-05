from datetime import datetime
from hashlib import md5
from time import time

import bcrypt,jwt
from flask import current_app
from flask_login import UserMixin
from flask_pymongo import ObjectId

from ext import login, mongo


class User(UserMixin):

    def __init__(self, name,passwd='passwd',post_num=0):
        self.name = name
        self.passwd = passwd
        self.post_num = post_num
        self.path = current_app.config['UPLOADED_DATA_DEST'] + '/' + str(name)
        self.admin = False

    def get_id(self):
        return self.name

    def get_post_num(self):
        users = mongo.db.users
        user = users.find_one({'name': self.name})
        if 'post_num' not in user.keys():
            user['post_num'] = 0
            users.save(user)
        return user['post_num']

    def get_admin(self):
        users = mongo.db.users
        user = users.find_one({'name': self.name})
        if 'admin' not in user.keys():
            user['admin'] = False
            users.save(user)
        return user['admin']

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
        hash_pass = bcrypt.hashpw(self.passwd.encode('utf-8'), bcrypt.gensalt())
        digest = md5(self.name.lower().encode('utf-8')).hexdigest()
        size =256
        avatar ='https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        users.insert({
            'name': self.name,
            "passwd": hash_pass,
            "post_num": self.post_num,
            "admin": self.admin,
            "pass":False,
            "avatar": avatar,
        })

    def set_post_num(self,num):
        users = mongo.db.users
        user = users.find_one({'name':self.name})
        user['post_num'] = num
        users.save(user)


    def validate_login(self):
        users = mongo.db.users
        user = users.find_one({'name': self.name})
        passwd = user['passwd']
        passwd_hash = bcrypt.hashpw(self.passwd.encode('utf-8'), passwd)
        return passwd_hash == passwd

    @staticmethod
    def verify_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        users = mongo.db.users
        return users.find_one({'name': id})
        

class Post(UserMixin):
    def __init__(self,name,post_1=None,post_2=None,post_3=None):
        self.name = name
        self.post_1 = post_1
        self.post_2 = post_2
        self.post_3 = post_3
    def submit(self):
        users = mongo.db.users
        user = users.find_one({'name': self.name})
        posts = {
                'post_1':self.post_1,
                'post_2':self.post_2,
                'post_3':self.post_3,
            }
        if 'posts' not in user.keys():
            user['posts']=posts
        else:
            for x in posts:
                if posts[x]:
                    user['posts'][x]=posts[x]
        users.save(user)


@login.user_loader
def load_user(name):
    users = mongo.db.users
    user = users.find_one({'name': name})
    if user:
        return User(name)
    return user
