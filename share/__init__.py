from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SHARE_DATABASE')
app.config['SECRET_KEY']=os.getenv('SHARE_KEY')
db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)

from share import routes