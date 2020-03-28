from datetime import datetime, date
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


class Tecnico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)

    oss = db.relationship("Os", backref="tecnico", lazy=True)

    def __repr__(self):
        return f"Tecnico('{self.nome}')"


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(12), nullable=True)
    celular = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(25), nullable=True)
    bairro = db.Column(db.String(25), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)

    oss = db.relationship("Os", backref="cliente", lazy=True)

    def __repr__(self):
        return f"Client('{self.cpf}', '{self.nome}', '{self.email}, '{self.cep}', '{self.endereco}', '{self.numero}', '{self.bairro}', '{self.cidade}', '{self.estado}')"


class Os(db.Model):
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

    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    id_tecnico = db.Column(db.Integer, db.ForeignKey("tecnico.id"), nullable=True) 

    orcamento = db.relationship("Orcamento", backref="os", lazy=True, uselist=False)

    equipamentos = db.relationship("Equipamento", backref="os", lazy=True)
    pecas = db.relationship("Peca", backref="os", lazy=True)

    def __repr__(self):
        return f"OS('{self.numero}', '{self.status}', '{self.data_entrega}'"


class Orcamento(db.Model):
    mao_de_obra = db.Column(db.Float, nullable=False)
    valor_total_pecas = db.Column(db.Float, nullable=False)
    imposto_sobre_servico = db.Column(db.Float, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)


    numero_os = db.Column(db.Integer, db.ForeignKey("os.numero"), primary_key=True)


class Equipamento(db.Model):
    nro_de_serie = db.Column(db.String(20), nullable=True)
    capacidade = db.Column(db.Float, nullable=True)
    lacre_entrada = db.Column(db.Boolean, nullable=False)
    lacre_saida = db.Column(db.Boolean, nullable=True)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)

    numero = db.Column(db.Integer, primary_key=True)
    numero_os = db.Column(db.Integer, db.ForeignKey("os.numero"), primary_key=True)

    def __repr__(self):
        return f"Equipamento('{self.nro_de_serie}', '{self.marca}', '{self.modelo}')"

class Peca(db.Model):
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(120), nullable=True)
    marca = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(30), nullable=False)
    valor_unitario = db.Column(db.Float, nullable=False)

    numero = db.Column(db.Integer, primary_key=True)
    numero_os = db.Column(db.Integer, db.ForeignKey("os.numero"), primary_key=True)

    def __repr__(self):
        return f"Peca('{self.marca}', '{self.nome}', '{self.valor_unitario}', '{self.quantidade}')"

# Faltou incluir a tabela Lancamento
# teste c1 = Cliente(cpf='44140912847', nome='Daniel', email='daniel@gmail.com', cep="007", endereco="endereco1", numero="1", bairro="bairro1", cidade="cidade1", estado="estado1")
