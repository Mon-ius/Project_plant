from flask_babel import _
from flask_login import  login_user, logout_user, current_user, login_required


from flask import render_template, redirect, url_for, flash, request
from app.auth.forms import LoginForm, RegistrationForm, ResetRequestForm, ResetPasswordForm

from app.admin import bp
from app.models import User
from ext import mongo.db as db


@bp.route('/')
@login_required
def index():
    if current_user.get_admin():
        users = db.users
        user = users.find({"post_num": {"$gt": 0}})
        return render_template('admin/index.html', users=user, admin=True)
    return redirect(url_for('main.index'))

@bp.route('/exports/<username>', methods=['POST', 'GET'])
@login_required
def export(username):
    if current_user.get_admin():
        users = db.users
        user = users.find({"name": username})
        return render_template('admin/export.html', users=user, admin=True)
    return redirect(url_for('main.index'))


@bp.route('/exports', methods=['POST', 'GET'])
@login_required
def export_all():
    if current_user.get_admin():
        users = db.users
        user = users.find({"post_num": {"$gt": 0}})
        return render_template('admin/export.html', users=user, admin=True)
    return redirect(url_for('main.index'))
