from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
                    validators=[DataRequired(), Email()])

    password = PasswordField('Senha', 
                    validators=[DataRequired()])

    confirm_password = PasswordField('Confirmar Senha', 
                    validators=[DataRequired(), EqualTo('senha')])

    submit = SubmitField('Cadastrar')


class LoginForm(FlaskForm):
    
    email = StringField('Email', 
                    validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
                    validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


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

