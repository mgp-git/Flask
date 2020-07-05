from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from ..models.models import User

class RegisterForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired(), Length(min=3, max=32)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=4, max=32)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message="Passowrds do not match")])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Submit')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already registered, please login")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("username is already registered")
