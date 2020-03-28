from flask import render_template, url_for, flash, redirect, request
from osmanager import app, db, bcrypt
from osmanager.forms import RegistrationForm, LoginForm, UpdateAccountForm ,ClientForm
from osmanager.models import User, Cliente
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sua conta foi criada!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Por Favor verifique seu email e a senha', 'danger')
    return render_template("login.html", title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Sua conta foi atualizada!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data == current_user.username
        form.email.data == current_user.email
    return render_template("account.html", title='Account', form=form)


@app.route('/client', methods=['GET', 'POST'])
def client():
    form = ClientForm()
    return render_template("client.html", title='Novo Cliente', form=form)

