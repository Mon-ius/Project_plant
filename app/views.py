 #coding:utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, mongo, lm
from .forms import LoginForm
import bcrypt



@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index_test.html')


@app.route('/login', methods = ['POST','GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})
        
        if login_user:
            if bcrypt.hashpw(request.form['passwd'].encode('utf-8'),login_user['passwd']) == login_user['passwd']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        return u'账号或密码错误'
    return render_template('login.html',
        title = '登录',
        form=form)
        
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = LoginForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['passwd'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name': request.form['username'],"passwd":hashpass })
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'that is already exited'
    return render_template('register.html',
        title = '注册',
        form=form)

@app.route('/input_0')
def input_0():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('input0.html')
@app.route('/input_1')
def input_1():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('input1.html')
@app.route('/input_2')
def input_2():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('input2.html')
@app.route('/input_3')
def input_3():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('input3.html')

