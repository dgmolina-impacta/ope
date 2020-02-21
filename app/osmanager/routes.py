from flask import render_template, url_for, flash, redirect
from osmanager import app
from osmanager.forms import RegistrationForm, LoginForm, ClientForm
from osmanager.models import User, Client

os = {"numero": "xxxxx",
    "cliente": "Daniel Gomes Molina",
    "equipamento": "Balança Filizola",
    "status": "Em manutenção"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", os=os)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta Criada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

@app.route('/client', methods=['GET', 'POST'])
def client():
    form = ClientForm()
    return render_template("client.html", title='Novo Cliente', form=form)