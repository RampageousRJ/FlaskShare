from share import app,db
from flask import render_template,flash,redirect,url_for,request,send_file
from flask_bcrypt import check_password_hash
from flask_login import current_user,login_user,login_required,logout_user
from share.forms import *
from share.models import *
from io import BytesIO
import os

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
    files = File.query.order_by(File.date_added.desc())
    return render_template('dashboard.html',files=files)

@login_required
@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    flash("Logged out successfully!")   
    return redirect(url_for('login'))

@login_required
@app.route('/upload',methods=['GET','POST'])
def upload():
    if current_user.type!='Admin':
        flash("You are not authorized to access this page!")
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    form = UploadForm()
    if request.method=='POST':
        uploaded_files = request.files.getlist("file")
        for file in uploaded_files:
            upload = File(filename=file.filename,data=file.read())
            db.session.add(upload)
            db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('upload.html',form=form)

@login_required
@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    if current_user.type!='Admin':
        flash("You are not authorized to access this page!")
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    file = File.query.get_or_404(id)
    try:
        db.session.delete(file)
        db.session.commit()
        flash("Deleted Successfully!")
    except:
        flash("Error in deleting! Please try again!")
    return redirect(url_for('dashboard'))

@login_required
@app.route('/download/<int:id>',methods=['GET'])
def download(id):
    if current_user.is_authenticated==False:
        flash("You are not authorized to access this page!")
        return redirect(url_for('login'))
    file = File.query.get_or_404(id)
    return send_file(BytesIO(file.data),download_name=file.filename,as_attachment=True)
            