from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,\
                    BooleanField
from wtforms.validators import DataRequired,ValidationError,\
                    Email,EqualTo

from flask_babel import _, lazy_gettext as _l
from ext import mongo.db as db


class LoginForm(FlaskForm):
    username = StringField(
        '学号/工号',
        validators=[
            DataRequired(message='学号不能为空'),
            Length(min=8, max=15, message='学号格式不正确')
        ])
    passwd = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember_me = BooleanField('记住我', default=False)
    submit = SubmitField('登录')

    def validate_username(self, username):
        users = db.users
        user = users.find_one({'name': username.data})
        if user is None:
            raise ValidationError('账号不存在')


class RegistrationForm(FlaskForm):
    username = StringField(
        '学号/工号',
        validators=[
            DataRequired(message='学号不能为空'),
            Length(min=8, max=15, message='学号格式不正确')
        ])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    passwd2 = PasswordField(
        '重复密码',
        validators=[
            DataRequired(message='请输入重复密码'),
            EqualTo('passwd', message='密码不正确')
        ])
    submit = SubmitField('注册')

    def validate_username(self, username):
        users = db.users
        user = users.find_one({'name': username.data})
        if user is not None:
            raise ValidationError('该学号已经被注册')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    passwd = PasswordField(_l('Password'), validators=[DataRequired()])
    passwd2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('passwd')])
    submit = SubmitField(_l('Request Password Reset'))
