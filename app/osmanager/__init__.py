from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from osmanager.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from osmanager.clientes.routes import clientes
    from osmanager.main.routes import main
    from osmanager.ordens.routes import ordens
    from osmanager.erros.handlers import erros
    app.register_blueprint(clientes)
    app.register_blueprint(main)
    app.register_blueprint(ordens)
    app.register_blueprint(erros)

    return app