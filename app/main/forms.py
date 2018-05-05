from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,\
                    BooleanField, TextAreaField,FieldList
from wtforms.validators import DataRequired,ValidationError,\
                    Email,EqualTo,Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

from ext import mongo


class ProfileForm(FlaskForm):
    realname = StringField(
        '姓名', validators=[DataRequired(),
                            Length(min=1, max=10)])
    phonenumber = StringField(
        '手机号码', validators=[DataRequired(),
                            Length(min=1, max=20)])
    school = StringField(
        '院校名称', validators=[DataRequired(),
                           Length(min=1, max=10)])
    college = StringField(
        '所在学院', validators=[DataRequired(),
                            Length(min=1, max=10)])
    state = StringField(
        '职称', validators=[DataRequired(),
                            Length(min=1, max=10)])
    info = TextAreaField(
        '个人简介', validators=[DataRequired(),
                            Length(min=1, max=233)])
    # upload_begin = FieldList(FileField('材料提交'))
    submit = SubmitField('提交')

class PostForm(FlaskForm):
    stage = StringField(
        '项目阶段', validators=[DataRequired(),
                            Length(min=1, max=3)])
    passed = BooleanField(
        '通过', validators=[DataRequired(),
                            Length(min=1, max=4)])
    submit = SubmitField('提交')

class BeginForm(FlaskForm):
    pname = StringField(
        '项目名称', validators=[DataRequired(),
                            Length(min=1, max=30)])
    pclass = StringField(
        '所属项目类别', validators=[DataRequired(),
                            Length(min=1, max=10)])
    college = StringField(
        '所在学院', validators=[DataRequired(),
                            Length(min=1, max=10)])
    person = StringField(
        '负责人', validators=[DataRequired(),
                           Length(min=1, max=10)])
    teacher = StringField(
        '指导老师', validators=[DataRequired(),
                           Length(min=1, max=10)])
    post = TextAreaField(
        '项目简介', validators=[DataRequired(),
                            Length(min=1, max=500)])
    # upload_begin = FieldList(FileField('材料提交'))

    upload = FileField(
        '材料提交',
        validators=[
            FileRequired(),
            FileAllowed(['doc', 'docx', 'pdf'], message='请提交正确的文档')
        ])
    submit = SubmitField('提交')


class MiddleForm(FlaskForm):
    level = StringField(
            '项目级别', validators=[DataRequired(),
                                Length(min=1, max=10)])
    money = StringField(
            '经费需求', validators=[DataRequired(),
                                Length(min=1, max=10)])
    team = StringField(
        '团队信息', validators=[DataRequired(),
                            Length(min=1, max=30)])
    upload = FileField(
        '材料提交',
        validators=[
            FileRequired(),
            FileAllowed(['doc', 'docx', 'pdf'], '请提交正确的文档')
        ])
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
