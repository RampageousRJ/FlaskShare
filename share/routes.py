from share import app,db
from flask import render_template,flash,redirect,url_for,request
from flask_bcrypt import check_password_hash
from flask_login import current_user,login_user,login_required,logout_user
from share.forms import *
from share.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method=='POST':
        mail_exists = People.query.filter_by(email=form.email.data).first()
        name_repeat = People.query.filter_by(username=form.username.data).first()
        if name_repeat:
            flash("Username already exists! Try logging in or using a different ID.")
            return render_template('register.html',form=form)
        if mail_exists:
            flash("Email already exists! Try logging in or using a different ID.")
            return render_template('register.html',form=form)
        u1 = People(username=form.username.data,email=form.email.data,password=form.password_hash.data,type=request.form['radio'])
        db.session.add(u1)
        db.session.commit()
        flash("User Registered Successfully!")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = People.query.filter_by(username=form.username.data).first()
        if user:
            if user.verify_password(form.password.data):
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

@login_required
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    print(current_user.id)
    logout_user()
    return render_template('dashboard.html')