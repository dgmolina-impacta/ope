from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from osmanager.models import Cliente



class SearchSOForm(FlaskForm):
    opcao_busca = SelectField('Procurar por', choices=[("cpf", "CPF"), ("numero_os", "Número da OS"), ("status", "Status")])

    valor_busca = StringField('', validators=[DataRequired(message="Campo obrigatório."), Length(max=30)])

    submit = SubmitField('Buscar')

class NewSOForm(FlaskForm):
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired(message="Campo obrigatório.")])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(message="Campo obrigatório."), Length(max=200)])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20)])
    
    capacidade = DecimalField("Capacidade (Quilogramas):")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório."), Length(max=20)])

    modelo = StringField("* Modelo:", validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])


class AddComponentForm(FlaskForm):
    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório."), Length(max=30)])

    nome = StringField("* Nome:", validators=[DataRequired(message="Campo obrigatório."), Length(max=30)])

    valor_unitario = DecimalField("** Valor Unitário:", validators=[DataRequired(message="Campo obrigatório.")])

    quantidade = IntegerField("* Quantidade:", validators=[DataRequired(message="Campo obrigatório.")])

    submit = SubmitField("Adicionar")


class FullRegisterForm(FlaskForm):
    # Cliente
    cpf = StringField('CPF:',
                      validators=[DataRequired(message="Campo obrigatório."), Length(min=11, max=11)])

    name = StringField('Nome:',
                       validators=[DataRequired(message="Campo obrigatório."), Length(min=2, max=100, )])

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

    # OS
    data_entrada = DateField('* Data de Entrada:', validators=[DataRequired(message="Campo obrigatório.")])

    tipo_defeito = StringField("* Tipo de defeito:", validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])

    problema_informado = TextAreaField("* Problema informado:", validators=[DataRequired(message="Campo obrigatório."), Length(max=200)])

    submit = SubmitField("Registrar")

    # Equipamento
    nro_de_serie = StringField("Número de Série:", validators=[Length(max=20)])
    
    capacidade = DecimalField("Capacidade (Quilogramas):")

    lacre_entrada = SelectField("* Lacre na entrada:", choices=[("sim", "Sim"), ("nao", "Não")])

#    lacre_saida = SelectField("* Lacre na saída:", choices=[("sim", "Sim"), ("nao", "Não")])

    marca = StringField("* Marca:", validators=[DataRequired(message="Campo obrigatório."), Length(max=20)])

    modelo = StringField("* Modelo:", validators=[DataRequired(message="Campo obrigatório."), Length(max=50)])

    def validate_cpf(self, cpf):
        cliente = Cliente.query.filter_by(cpf=cpf.data).first()
        if cliente:
            raise ValidationError('Já existe um registro com este CPF. Por favor, verifique o registro existente.')

class UpdateSoForm(FlaskForm):

    status = SelectField("Status:", choices=[("Aberta", "Aberta"), ("Orçamento Aprovado", "Orçamento Aprovado"), ("Finalizada", "Finalizada")])
    
    problema_constatado = TextAreaField("Problema constatado:", validators=[Length(max=200)])

    mao_de_obra = DecimalField("Mão de Obra:")

    desconto = DecimalField("Desconto:")

    submit = SubmitField("Alterar")

class CloseSoForm(FlaskForm):

    status = SelectField("Status:", choices=[("Finalizada", "Finalizada")])
    
    problema_constatado = TextAreaField("Problema constatado:", validators=[Length(max=200)])

    mao_de_obra = DecimalField("Mão de Obra:")

    desconto = DecimalField("Desconto:")

    forma_de_pagamento = SelectField("Forma de pagamento:", choices=[("Dinheiro", "Dinheiro"), ("Cartão", "Cartão")])

    garantia = DateField('Garantia:')

    data_saida = DateField("Data de Saída:")

    submit = SubmitField("Finalizar")

