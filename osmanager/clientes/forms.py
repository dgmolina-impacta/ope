from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email




class ClientForm(FlaskForm):
    cpf = StringField('CPF (Sem pontuação):',
                      validators=[DataRequired(message="Campo obrigatório"), Length(min=11, max=11, message="Entre com 11 Digitos (Sem pontuação)")])
    
    name = StringField('Nome:', 
                       validators=[DataRequired(message="Campo obrigatório"), Length(min=2, max=100, message="Digite entre 2 e 100 caracteres")])
    
    phone = StringField('Tel. Fixo:',
                        validators=[Length(min=8, max=20, message="Dite no mínimo 8 números")])

    mobile = StringField('Celular:', 
                         validators=[DataRequired(message="Campo obrigatório"), Length(min=9, max=20, message="Digite no mínimo 9 números")])

    email = StringField('Email:', 
                        validators=[DataRequired(message="Campo obrigatório"), Email(), Length(max=100, message="Digite no máximo 100 caracteres")])

    cep = StringField('CEP:', 
                      validators=[DataRequired(message="Campo obrigatório"), Length(min=8, max=9, message="Digite no máximo 9 caracteres")])
    
    address = StringField('Endereço:', 
                          validators=[DataRequired(message="Campo obrigatório"), Length(max=150, message="Digite no máximo 150 caracteres")])

    number = StringField('Número:', 
                         validators=[DataRequired(message="Campo obrigatório"), Length(max=5, message="Maior número aceito (99999)")])
    
    complement = StringField('Complemento:', validators=[Length(max=50, message="Digite no máximo 50 caracteres")])

    neighborhood = StringField('Bairro:',
                               validators=[DataRequired(message="Campo obrigatório"), Length(max=25, message="Digite no máximo 25 caracteres")])

    city = StringField('Cidade:', 
                       validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])
    
    state = StringField('Estado:', 
                        validators=[DataRequired(message="Campo obrigatório"), Length(min=2, max=2, message="UF - exemplo: SP")])

    submit = SubmitField('Cadastrar')

class SearchClientForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("nome", "Nome")])
    
    valor_busca = StringField('', validators=[DataRequired(message="Campo obrigatório"), Length(min=2, max=30, message="Digite no mínimo 2 e no máximo 30 caracteres")])

    submit = SubmitField('Buscar')

class CheckCPFForm(FlaskForm):
    check_cpf_sub = SubmitField("Consultar")

    check_cpf_field = StringField('CPF:',
                                  validators=[DataRequired(message="Campo obrigatório"), Length(min=11, max=11, message="Entre com 11 Digitos (Sem pontuação)")])

class UpdateClientForm(FlaskForm):
    phone = StringField('Telefone',
                        validators=[Length(min=8, max=20, message="Dite no mínimo 8 números")])

    mobile = StringField('Celular', 
                         validators=[DataRequired(message="Campo obrigatório"), Length(min=9, max=20, message="Digite no mínimo 9 números")])

    email = StringField('Email', 
                        validators=[DataRequired(message="Campo obrigatório"), Email(), Length(max=100, message="Digite no máximo 100 caracteres")])

    cep = StringField('CEP', 
                      validators=[DataRequired(message="Campo obrigatório"), Length(min=8, max=9, message="Digite no máximo 9 caracteres")])

    address = StringField('Endereço', 
                          validators=[DataRequired(message="Campo obrigatório"), Length(max=150, message="Digite no máximo 150 caracteres")])

    number = StringField('Número', 
                         validators=[DataRequired(message="Campo obrigatório"), Length(max=5, message="Maior número aceito (99999)")])
    
    complement = StringField('Complemento', validators=[Length(max=50, message="Digite no máximo 50 caracteres")])

    neighborhood = StringField('Bairro',
                               validators=[DataRequired(message="Campo obrigatório"), Length(max=25, message="Digite no máximo 25 caracteres")])

    city = StringField('Cidade', 
                       validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])
    
    state = StringField('Estado', 
                        validators=[DataRequired(message="Campo obrigatório"), Length(min=2, max=2, message="UF - exemplo: SP")])

    submit = SubmitField('Atualizar')
