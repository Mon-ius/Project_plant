
import os

from flask_babel import _
from flask_login import current_user, login_required


from flask import render_template, redirect, url_for, flash, request,abort
from app.main.forms import PostForm, ProfileForm, BeginForm, MiddleForm, FinalForm

from app.main import bp

from app.models import User, Post
from ext import mongo

from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.get_admin():
        return redirect(url_for('admin.index'))
    return render_template('Index.html')


@bp.route('/post', methods=['GET', 'POST'])
def post():
    if not current_user.get_admin():
        return redirect(url_for('index'))
    form = PostForm()
    if form.validate_on_submit():
        stage=int(form.data.stage)
        users = mongo.db.users
        user = users.find_one({'name': form.username.data})
        user['projects'][stage]['passed'] = True
        users.save(user)
        return redirect(url_for('profile', username=form.username.data))
    return abort(404)


@bp.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    if not current_user.get_admin():
        return redirect(url_for('index'))
    form = ProfileForm()
    users = mongo.db.users
    user = users.find_one({'name': username})
    if 'pass' not in user.keys():
        user['passed'] = False
        mongo.db.users.save(user)
    post = user['pass']
    if not user or user['post_num'] < 1:
        abort(404)
    return render_template(
        'Profile.html',
        forms=user['posts'],
        form=form,
        post=post,
        username=username,
        admin=False)


@bp.route('/info/<page>')
@login_required
def info(page):
    if page not in ['college', "class", "money", "preresult", "proccess", "accept", "finish", "eval"]:
        abort(404)
    return '功能正在完善'


@bp.route('/input_0', methods=['GET', 'POST'])
@login_required
def input_0():
    if current_user.get_admin():
        return redirect(url_for('admin'))
    return render_template('waitting.html')


@bp.route('/input_1', methods=['GET', 'POST'])
@login_required
def input_1():
    if current_user.get_admin():
        return redirect(url_for('admin'))
    if current_user.get_post_num() > 0:
        return redirect(url_for('input_0'))
    form = BeginForm()
    if form.validate_on_submit():
        file = form.__class__.__name__ + '-'+secure_filename(
            form.upload.data.filename)
        file_path = current_user.path
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        filedata = os.listdir(file_path)
        if file not in filedata:
            filedata.append(file)
            form.upload.data.save(file_path + '/' + file)

        post = {
            'project': form.project.data,
            'person': form.person.data,
            'money': form.money.data,
            'post': form.post.data,
            'upload': filedata,
        }
        p = Post(current_user.name, post_1=post)
        p.submit()
        current_user.set_post_num(1)
        return redirect(url_for('input_0'))
    return render_template('BeginForm.html', title='项目申请', form=form)


@bp.route('/input_2', methods=['GET', 'POST'])
@login_required
def input_2():
    if current_user.get_admin():
        return redirect(url_for('admin'))
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
        if file not in filedata:
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


@bp.route('/input_3', methods=['GET', 'POST'])
@login_required
def input_3():
    if current_user.get_admin():
        return redirect(url_for('admin'))
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
        if file not in filedata:
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



