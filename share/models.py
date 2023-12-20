from share import app,db
from flask_bcrypt import check_password_hash,generate_password_hash

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    password_hash = 