 #coding:utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User


def had_sigin():
    return False
@app.route('/')
def index():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    if  form.validate_on_submit():
        
        return redirect('/index')
    else:
        return render_template('login.html',
        title = '登录',
        form = form)
@app.route('/input_0')
def input_0():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input0.html')
@app.route('/input_1')
def input_1():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input1.html')
@app.route('/input_2')
def input_2():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input2.html')
@app.route('/input_3')
def input_3():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input3.html')

