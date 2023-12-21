from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired, EqualTo,Length
from flask_login import UserMixin

class RegisterForm(UserMixin,FlaskForm):
    username=StringField("Enter username: ",validators=[DataRequired()])
    email=EmailField("Enter email: ",validators=[DataRequired()])
    password_hash=PasswordField("Enter password: ",validators=[DataRequired(),EqualTo('password_hash2',message='Passwords must match'),Length(8)])
    password_hash2=PasswordField("Re-type password: ",validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit=SubmitField("Submit")
    
class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')