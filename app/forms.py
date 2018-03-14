from flask_uploads import UploadSet
from flask_wtf import FlaskForm
from flask_login import  current_user
from wtforms import StringField, PasswordField, SubmitField,\
                    BooleanField, TextAreaField,FieldList
from wtforms.validators import DataRequired,ValidationError,\
                    Email,EqualTo,Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

from app import mongo
# from app.models import User


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
        users = mongo.db.users
        user = users.find_one({'name': username.data})
        if user is  None:
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

    def validate_username(self,username):
        users = mongo.db.users
        user = users.find_one({'name': username.data})
        if user is not None:
            raise ValidationError('该学号已经被注册')



    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')


class ProfileForm(FlaskForm):
    username = StringField('学号/工号', validators=[DataRequired()])
    submit = SubmitField('审核通过')


class BeginForm(FlaskForm):
    project = StringField('项目名称', validators=[DataRequired(),Length(min=1, max=30)])
    person = StringField('负责人', validators=[DataRequired(),Length(min=1, max=10)])
    money = StringField('经费需求', validators=[DataRequired(),Length(min=1, max=10)])
    post = TextAreaField('项目概述', validators=[DataRequired(),Length(min=1, max=500)])
    # upload_begin = FieldList(FileField('材料提交'))


    upload = FileField('材料提交', validators=[FileRequired(),FileAllowed(['doc', 'docx','pdf'], message='请提交正确的文档')])
    submit = SubmitField('提交')





class MiddleForm(FlaskForm):
    schedule = StringField('项目进度', validators=[DataRequired(),Length(min=1, max=30)])
    preview = StringField('预期成果名称', validators=[DataRequired(),Length(min=1, max=100)])
    post = TextAreaField('阶段性报告', validators=[DataRequired(),Length(min=1, max=500)])
    upload = FileField('材料提交', validators=[FileRequired(),FileAllowed(['doc', 'docx','pdf'], '请提交正确的文档')])
    submit = SubmitField('提交')

    def validate_schedule(self, schedule):
        users = mongo.db.users
        user = users.find_one({'name': current_user.name})
        if not ('posts' in user.keys()):
            raise ValidationError('请提交项目申请')
        if user['posts']['post_1'] is None:
            raise ValidationError('请等待通过审核')

class FinalForm(FlaskForm):
    change = StringField(
        '研究目标变动情况', validators=[DataRequired(),
                                Length(min=1, max=30)])
    achievement = StringField(
        '取得成果', validators=[DataRequired(),
                            Length(min=1, max=100)])
    post = TextAreaField(
        '成果意义', validators=[DataRequired(),
                            Length(min=1, max=500)])
    upload = FileField(
        '论文，专利等',
        validators=[
            FileRequired(),
            FileAllowed(['doc', 'docx', 'pdf'], '请提交正确的文档')
        ])
    submit = SubmitField('提交')

    def validate_change(self, change):
        users = mongo.db.users
        user = users.find_one({'name': current_user.name})
        if not ('posts' in user.keys()):
            raise ValidationError('请提交项目申请')
        if user['posts']['post_2'] is None:
            raise ValidationError('需要完成中期材料提交并通过审核')






class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField('Request Password Reset')