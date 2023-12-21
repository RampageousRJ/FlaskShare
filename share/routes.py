from share import app,LoginManager,db
from flask import render_template,flash,redirect,url_for
from flask_bcrypt import check_password_hash
from flask_login import current_user,login_user
from share.forms import *
from share.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    pass

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = People.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash,form.password.data):
                login_user(user)
                flash("Logged in successfully!")
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Password! Please try a different password!")
        else:
            flash("Username does not exist!")  
    if current_user.is_authenticated:
        flash('ERROR: You are already logged in!')
        return redirect(url_for('dashboard'))             
    return render_template('login.html',form=form) 