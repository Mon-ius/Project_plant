#coding:utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required

from .forms import LoginForm, RegistrationForm, BeginForm, MiddleForm, FinalForm
from .models import User,Post
from werkzeug.utils import secure_filename
from app import app, mongo, login
import bcrypt,os



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('Index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods = ['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User(form.username.data,form.passwd.data)
        if not user.validate_login():
            flash('密码错误')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me)
        # login_user(User(str(user['_id'])))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('Login.html',
        title = '登录',
        form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data,form.passwd.data)
        user.set_passwd()
        flash('恭喜,你已经成为注册用户')
        return redirect(url_for('login'))
    return render_template('Register.html',
        title = '注册',
        form=form)


@app.route('/input_0', methods=['GET', 'POST'])
@login_required
def input_0():
    return render_template('waitting.html')


@app.route('/input_1', methods=['GET', 'POST'])
@login_required
def input_1():
    # if current_user.get_post_num()>0:
    #     return redirect(url_for('input_0'))
    form = BeginForm()
    if form.validate_on_submit():
        file = form.__class__.__name__ + '-'+secure_filename(
            form.upload.data.filename)
        file_path = current_user.path
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        filedata = os.listdir(file_path)
        filedata.append(file)
        form.upload.data.save(file_path + '/' + file)

        post = {
            'project': form.project.data,
            'person': form.person.data,
            'money': form.money.data,
            'post': form.post.data,
            'upload': filedata,
        }
        p=Post(current_user.name,post_1=post)
        p.submit()
        current_user.set_post_num(1)
        return redirect(url_for('input_0'))
    return render_template('BeginForm.html', title='项目申请',form=form)


@app.route('/input_2', methods=['GET', 'POST'])
@login_required
def input_2():
    if current_user.get_post_num() > 1:
        return redirect(url_for('input_0'))
    form = MiddleForm()
    if form.validate_on_submit():
        file = form.__class__.__name__ + '-' + secure_filename(
            form.upload.data.filename)
        file_path = current_user.path
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        filedata = os.listdir(file_path)
        filedata.append(file)
        form.upload.data.save(file_path + '/' + file)

        post = {
            'schedule': form.schedule.data,
            'preview': form.preview.data,
            'post': form.post.data,
            'upload': filedata,
        }
        p = Post(current_user.name, post_2=post)
        p.submit()
        current_user.set_post_num(3)
        return redirect(url_for('input_0'))
    return render_template('MiddleForm.html', title='中期检查', form=form)


@app.route('/input_3', methods=['GET', 'POST'])
@login_required
def input_3():
    if current_user.get_post_num() > 3:
        return redirect(url_for('input_0'))
    form = FinalForm()
    if form.validate_on_submit():
        file = form.__class__.__name__ + '-' + secure_filename(
            form.upload.data.filename)
        file_path = current_user.path
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        filedata = os.listdir(file_path)
        filedata.append(file)
        form.upload.data.save(file_path + '/' + file)
        post = {
            'change': form.change.data,
            'achievement': form.achievement.data,
            'post': form.post.data,
            'upload': filedata,
        }
        p = Post(current_user.name, post_3=post)
        p.submit()
        current_user.set_post_num(7)
        return redirect(url_for('input_0'))
    return render_template('FinalForm.html', title='成果验收', form=form)
