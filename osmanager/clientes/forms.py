from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email




class ClientForm(FlaskForm):
    cpf = StringField('CPF (Sem pontuação):',
                      validators=[DataRequired(message="Campo obrigatório."), Length(min=11, max=11)])
    
    name = StringField('Nome:', 
                       validators=[DataRequired(message="Campo obrigatório."), Length(min=2, max=100)])
    
    phone = StringField('Tel. Fixo:',
                        validators=[Length(max=20)])

    mobile = StringField('Celular:', 
                         validators=[DataRequired(message="Campo obrigatório."), Length(max=20)])

    email = StringField('Email:', 
                        validators=[DataRequired(message="Campo obrigatório."), Email(), Length(max=100)])

    cep = StringField('CEP:', 
                      validators=[DataRequired(message="Campo obrigatório."), Length(min=8, max=9)])
    
    address = StringField('Endereço:', 
                          validators=[DataRequired(message="Campo obrigatório."), Length(max=150)])

    number = StringField('Número:', 
                         validators=[DataRequired(message="Campo obrigatório."), Length(max=5)])
    
    complement = StringField('Complemento:', validators=[Length(max=50)])

    neighborhood = StringField('Bairro:',
                               validators=[DataRequired(message="Campo obrigatório."), Length(max=25)])

    city = StringField('Cidade:', 
                       validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])
    
    state = StringField('Estado:', 
                        validators=[DataRequired(message="Campo obrigatório."), Length(min=2, max=2, message="UF - exemplo: SP")])

    submit = SubmitField('Cadastrar')

class SearchClientForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("nome", "Nome")])
    
    valor_busca = StringField('', validators=[DataRequired(message="Campo obrigatório."), Length(min=2, max=30)])

    submit = SubmitField('Buscar')

class CheckCPFForm(FlaskForm):
    check_cpf_sub = SubmitField("Consultar")

    check_cpf_field = StringField('CPF:',
                                  validators=[DataRequired(message="Campo obrigatório."), Length(min=11, max=11)])

class UpdateClientForm(FlaskForm):
    phone = StringField('Telefone',
                        validators=[Length(max=20)])

    mobile = StringField('Celular', 
                         validators=[DataRequired(message="Campo obrigatório."), Length(max=20)])

    email = StringField('Email', 
                        validators=[DataRequired(message="Campo obrigatório."), Email(), Length(max=100)])

    cep = StringField('CEP', 
                      validators=[DataRequired(message="Campo obrigatório."), Length(min=8, max=9)])

    address = StringField('Endereço', 
                          validators=[DataRequired(message="Campo obrigatório."), Length(max=150)])

    number = StringField('Número', 
                         validators=[DataRequired(message="Campo obrigatório."), Length(max=5)])
    
    complement = StringField('Complemento', validators=[Length(max=50)])

    neighborhood = StringField('Bairro',
                               validators=[DataRequired(message="Campo obrigatório."), Length(max=25)])

    city = StringField('Cidade', 
                       validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])
    
    state = StringField('Estado', 
                        validators=[DataRequired(message="Campo obrigatório."), Length(min=2, max=2, message="UF - exemplo: SP")])

    submit = SubmitField('Atualizar')
