from flask import Blueprint
import click

from osmanager import db
from osmanager.models import User, Tecnico, Cliente, Os, Orcamento, Equipamento, Peca

cmd = Blueprint('cmd', __name__)

@cmd.cli.command('create_tables')
def create_tables():
    db.create_all()

@cmd.cli.command('drop_tables')
def drop_tables():
    db.drop_all()

