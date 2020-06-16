from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from osmanager.models import Cliente



class SearchSOForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("numero_os", "Número da OS"), ("status", "Status")])

    valor_busca = StringField('', validators=[DataRequired(message="Campo obrigatório"), Length(max=30, message="Digite no máximo 3 caracteres")])

    submit = SubmitField('Buscar')

class NewSOForm(FlaskForm):
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired(message="Campo obrigatório")])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Em andamento", "Em andamento"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(message="Campo obrigatório"), Length(max=200, message="Digite no máximo 200 caracteres")])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20, message="Digite no máximo 20 caracteres")])
    
    capacidade = DecimalField("Capacidade (Quilogramas):")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório"), Length(max=20, message="Digite no máximo 20 caracteres")])

    modelo = StringField("* Modelo:", validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])


class AddComponentForm(FlaskForm):
    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório"), Length(max=30, message="Digite no máximo 30 caracteres")])

    nome = StringField("* Nome:", validators=[DataRequired(message="Campo obrigatório"), Length(max=30, message="Digite no máximo 30 caracteres")])

    valor_unitario = DecimalField("** Valor Unitário:", validators=[DataRequired(message="Campo obrigatório")])

    quantidade = IntegerField("* Quantidade:", validators=[DataRequired(message="Campo obrigatório")])

    submit = SubmitField("Adicionar")


class FullRegisterForm(FlaskForm):
    # Cliente
    cpf = StringField('CPF (Sem pontuação):',
                      validators=[DataRequired(message="Campo obrigatório"), Length(min=11, max=11, message="Digite 11 caracteres (Sem pontuação)")])

    name = StringField('Nome:',
                       validators=[DataRequired(message="Campo obrigatório"), Length(min=2, max=100, message="Digite entre 2 e 100 caracteres")])

    phone = StringField('Tel. Fixo:',
                        validators=[Length(min=8, max=20, message="Digite no mínimo 8 números")])

    mobile = StringField('Celular:',
                         validators=[DataRequired(message="Campo obrigatório"), Length(min=9, max=20, message="Digite no mínimo 9 números")])

    email = StringField('Email:',
                        validators=[DataRequired(message="Campo obrigatório"), Email(), Length(max=100, message="Digite no máximo 100 caracteres")])

    cep = StringField('CEP:',
                      validators=[DataRequired(message="Campo obrigatório"), Length(min=8, max=9, message="Digite no mínimo 8 números")])

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

    # OS
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired(message="Campo obrigatório")])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(message="Campo obrigatório"), Length(max=200, message="Digite no máximo 200 caracteres")])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20, message="Digite no máximo 20 caracteres")])
    
    capacidade = DecimalField("Capacidade (Quilogramas):")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório"), Length(max=20, message="Digite no máximo 20 caracteres")])

    modelo = StringField("* Modelo:", validators=[DataRequired(message="Campo obrigatório"), Length(max=50, message="Digite no máximo 50 caracteres")])

    def validate_cpf(self, cpf):
        cliente = Cliente.query.filter_by(cpf=cpf.data).first()
        if cliente:
            raise ValidationError('Já existe um registro com este CPF. Por favor, verifique o registro existente.')

class UpdateSoForm(FlaskForm):

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Em andamento", "Em andamento"), ("Finalizada", "Finalizada")])
    
    problema_constatado = TextAreaField("Problema constatado:", validators=[Length(max=200, message="Digite no máximo 200 caracteres")])

    mao_de_obra = DecimalField("Mão de Obra:")

    desconto = DecimalField("Desconto:")

    submit = SubmitField("Alterar")

class CloseSoForm(FlaskForm):

    status = SelectField("Status:", choices=[("Finalizada", "Finalizada")])
    
    problema_constatado = TextAreaField("Problema constatado:", validators=[Length(max=200, message="Digite no máximo 200 caracteres")])

    mao_de_obra = DecimalField("Mão de Obra:")

    desconto = DecimalField("Desconto:")

    forma_de_pagamento = SelectField("Forma de pagamento:", choices=[("Dinheiro", "Dinheiro"), ("Cartão", "Cartão")])

    garantia = DateField('Garantia:')

    data_saida = DateField("Data de Saída:")

    submit = SubmitField("Finalizar")

