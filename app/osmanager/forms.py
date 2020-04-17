from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from osmanager.models import User, Cliente


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

    neighborhood = StringField('Bairro:',
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

class SearchSOForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("numero_os", "Número da OS")])

    valor_busca = StringField('', validators=[DataRequired(), Length(max=30)])

    submit = SubmitField('Buscar')

class NewSOForm(FlaskForm):
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired()])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(), Length(max=50)])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(), Length(max=200)])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20)])
    
    capacidade = DecimalField("Capacidade:")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(), Length(max=20)])

    modelo = StringField("* Modelo:", validators=[DataRequired(), Length(max=50)])


class AddComponentForm(FlaskForm):
    marca = StringField("* Marca:", validators=[DataRequired(), Length(max=30)])

    nome = StringField("* Modelo:", validators=[DataRequired(), Length(max=30)])

    valor_unitario = DecimalField("** Valor Unitário:", validators=[DataRequired()])

    quantidade = IntegerField("* Quantidade:", validators=[DataRequired()])

    submit = SubmitField("Adicionar")


class CheckCPFForm(FlaskForm):
    check_cpf_sub = SubmitField("Consultar")

    check_cpf_field = StringField('CPF:',
                                  validators=[DataRequired(), Length(min=11, max=11)])

class FullRegisterForm(FlaskForm):
    # Cliente
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

    neighborhood = StringField('Bairro:',
                               validators=[DataRequired()])

    city = StringField('Cidade:',
                       validators=[DataRequired()])

    state = StringField('Estado:',
                        validators=[DataRequired()])

    # OS
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired()])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(), Length(max=50)])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(), Length(max=200)])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20)])
    
    capacidade = DecimalField("Capacidade:")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(), Length(max=20)])

    modelo = StringField("* Modelo:", validators=[DataRequired(), Length(max=50)])

    def validate_cpf(self, cpf):
        cliente = Cliente.query.filter_by(cpf=cpf.data).first()
        if cliente:
            raise ValidationError('Já existe um registro com este CPF. Por favor, verifique o registro existente.')

