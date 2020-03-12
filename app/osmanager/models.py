from datetime import datetime
from osmanager import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    mobile = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    complement = db.Column(db.String(25), nullable=True)
    neighborhood = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f"Client('{self.cpf}', '{self.name}', '{self.phone}', '{self.mobile}', '{self.email}, '{self.cep}', '{self.address}', '{self.number}', '{self.complement}', '{self.neighborhood}', '{self.city}', '{self.state}')"