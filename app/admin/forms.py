from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired,ValidationError,Email,Length

class PassForm(FlaskForm):
    username = StringField('学号/工号', validators=[DataRequired()])
    submit = SubmitField('审核通过')