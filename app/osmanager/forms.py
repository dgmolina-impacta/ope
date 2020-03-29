from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from osmanager.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
                    validators=[DataRequired(), Email()])

    password = PasswordField('Senha', 
                    validators=[DataRequired()])

    confirm_password = PasswordField('Confirmar Senha', 
                    validators=[DataRequired(), EqualTo('password')])

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
                    validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
                    validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
                    validators=[DataRequired(), Email()])

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


class ClientForm(FlaskForm):
    cpf = StringField('CPF:', 
                    validators=[DataRequired(), Length(min=11, max=11)])
    
    name = StringField('Nome:', 
                    validators=[DataRequired(), Length(min=2, max=100)])
    
    phone = StringField('Tel. Fixo:')

    mobile = StringField('Celular:', 
                    validators=[DataRequired()])

    email = StringField('Email:', 
                    validators=[DataRequired(), Email()])

    cep = StringField('CEP:', 
                    validators=[DataRequired()])
    
    address = StringField('Endereço:', 
                    validators=[DataRequired()])

    number = StringField('Número:', 
                    validators=[DataRequired()])
    
    complement = StringField('Complemento:')

    neighborhood = StringField ('Bairro:',
                    validators=[DataRequired()])

    city = StringField('Cidade:', 
                    validators=[DataRequired()])
    
    state = StringField('Estado:', 
                    validators=[DataRequired()])

    submit = SubmitField('Cadastrar')

class SearchClientForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("nome", "Nome")])
    
    valor_busca = StringField('', validators=[DataRequired(), Length(min=2, max=30)])

    submit = SubmitField('Buscar')