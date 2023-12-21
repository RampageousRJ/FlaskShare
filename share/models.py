from share import db,bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return People.query.get(int(id))

class People(db.Model,UserMixin):
    __tablename__='people'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    password_hash2 = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)
    
    def verify_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f"<{self.username}>"