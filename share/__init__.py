from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SHARE_DATABASE')
app.config['SECRET_KEY']=os.getenv('SHARE_KEY')
app.config['RECAPTCHA_PUBLIC_KEY']=os.getenv('SHARE_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY']=os.getenv('SHARE_PRIVATE_KEY')
db.init_app(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"
moment = Moment(app)

from share import routes