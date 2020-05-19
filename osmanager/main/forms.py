from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from osmanager.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(message="Campo brigatório."), Length(min=2, max=20)])
    
    email = StringField('Email', 
                    validators=[DataRequired(message="Campo brigatório."), Email(), Length(max=100)])

    password = PasswordField('Senha', 
                    validators=[DataRequired(message="Campo brigatório."), Length(max=60)])

    confirm_password = PasswordField('Confirmar Senha', 
                    validators=[DataRequired(message="Campo brigatório."), EqualTo('password', message="As senhas não batem."), Length(max=60)])

    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Esse nome de usuário já existe. Por favor, escolha outro.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Esse email já existe. Por favor, escolha outro.')


class LoginForm(FlaskForm):
    
    email = StringField('Email', 
                    validators=[DataRequired(message="Campo brigatório."), Email(), Length(max=100)])

    password = PasswordField('Password', 
                    validators=[DataRequired(message="Campo brigatório."), Length(max=60)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(message="Campo brigatório."), Length(min=2, max=20)])
    
    email = StringField('Email', 
                    validators=[DataRequired(message="Campo brigatório."), Email(message="Email inválido."), Length(max=100)])

    submit = SubmitField('Atualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Esse nome de usuário já existi. Por favor, escolha outro.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Esse email já existi. Por favor, escolha outro.')