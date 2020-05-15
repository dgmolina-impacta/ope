from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email




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

class CheckCPFForm(FlaskForm):
    check_cpf_sub = SubmitField("Consultar")

    check_cpf_field = StringField('CPF:',
                                  validators=[DataRequired(), Length(min=11, max=11)])