from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SECRET_KEY'] = '732c3eeec9fb75e61d6edc6458d2faad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///site.db'
db = SQLAlchemy(app)

from osmanager import routes