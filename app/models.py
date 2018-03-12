from app import app, login, mongo
from flask_login import UserMixin
from flask_pymongo import ObjectId
import bcrypt


class User(UserMixin):

    def __init__(self, name,passwd='passwd',post_num=0):
        self.name = name
        self.passwd = passwd
        self.post_num = post_num
        self.path = app.config['UPLOADED_DATA_DEST'] + '/' + str(name)

    def get_id(self):
        return self.name

    def get_post_num(self):
        users = mongo.db.users
        user = users.find_one({'name': self.name})
        if 'set_post_num' not in user.keys():
            user['set_post_num']=0
            users.save(user)
        return user['set_post_num']

    def set_passwd(self):
        users = mongo.db.users
        hash_pass = bcrypt.hashpw(self.passwd.encode('utf-8'), bcrypt.gensalt())
        users.insert({
            'name': self.name,
            "passwd": hash_pass,
            "post_num": self.post_num
        })

    def set_post_num(self,num):
        users = mongo.db.users
        user = users.find_one({'name':self.name})
        user['set_post_num']=num
        users.save(user)


    def validate_login(self):
        users = mongo.db.users
        passwd = users.find_one({'name': self.name})['passwd']
        passwd_hash = bcrypt.hashpw(self.passwd.encode('utf-8'), passwd)
        return passwd_hash == passwd

@login.user_loader
def load_user(name):
    users = mongo.db.users
    user = users.find_one({'name': name})
    if user:
        return User(name)
    return user


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