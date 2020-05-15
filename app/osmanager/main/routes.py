from flask import render_template, url_for, flash, redirect, request, Blueprint
from osmanager import db, bcrypt
from osmanager.main.forms import RegistrationForm, LoginForm, UpdateAccountForm
from osmanager.models import User
from flask_login import login_user, current_user, logout_user, login_required


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html")

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Sua conta foi criada!', 'success')
        return redirect(url_for('main.login'))
    return render_template("register.html", title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Por Favor verifique seu email e a senha', 'danger')
    return render_template("login.html", title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Sua conta foi atualizada!', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        print(f"{form.username.data} and {form.email.data}")
    return render_template("account.html", title='Account', form=form)
