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


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
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


# Falta adicionar os valores em nullable
class OS(db.Model):
    numero = db.Column(db.Integer, primary_key=True)

    data_entrega = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date, nullable=True)
    desconto = db.Column(db.Float, nullable=True)
    garantia = db.Column(db.Date, nullable=True)
    problema_constatado = db.Column(db.String(200), nullable=True)
    problema_informado = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    tipo_defeito = db.Column(db.String(50), nullable=False)
    tipo_pagamento = db.Column(db.String(20), nullable=True)
    valor_produtos = db.Column(db.Float, nullable=True)
    valor_servicos = db.Column(db.Float, nullable=True)
    valor_total = db.Column(db.Float, nullable=True)

    client_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    client = db.relationship("Cliente", backref=db.backref("oss", lazy=True))
