from share import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    pass