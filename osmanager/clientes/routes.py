from flask import render_template, url_for, flash, redirect, request, Blueprint
from osmanager import db
from osmanager.clientes.forms import ClientForm, SearchClientForm, CheckCPFForm, UpdateClientForm
from osmanager.models import Cliente, Os
from flask_login import login_required


clientes = Blueprint('clientes', __name__)

@clientes.route('/register/client', methods=['GET', 'POST'])
@login_required
def register_client():
    form = ClientForm()
    if form.validate_on_submit():
        registro = Cliente(cpf=form.cpf.data, nome=form.name.data, 
                           telefone=form.phone.data, 
                           celular=form.mobile.data, email=form.email.data,
                           cep=form.cep.data, endereco=form.address.data,
                           numero=form.number.data, complemento=form.complement.data,
                           bairro=form.neighborhood.data, cidade=form.city.data,
                           estado=form.state.data)
        db.session.add(registro)
        db.session.commit()
        flash("O cliente foi registrado com sucesso", "success")
        return redirect(url_for("main.home"))
    return render_template("client.html", title='Novo Cliente', form=form)


@clientes.route('/search/client', methods=['GET', 'POST'])
@login_required
def search_client():
    form = SearchClientForm()
    page = request.args.get("page", 1, type=int)
    per_page = 2

    if form.validate_on_submit():
        opcao_busca = form.opcao_busca.data
        valor_busca = form.valor_busca.data
        page = 1 # reseta numero da pagina ao pesquisar
    else:
        opcao_busca = request.args.get("opcao_busca", None, type=str)
        valor_busca = request.args.get("valor_busca", None, type=str)

    if not (opcao_busca or valor_busca):
        clientes = Cliente.query.order_by(Cliente.nome.asc()).paginate(
                                                                      page=page,
                                                                      per_page=per_page)
    else:
        if opcao_busca == "cpf":    
            clientes = Cliente.query.filter_by(cpf=valor_busca).paginate(
                                                                        page=page,
                                                                        per_page=per_page)
        else:
            clientes = Cliente.query.filter(db.text(f"nome LIKE '%{valor_busca}%'")).order_by(Cliente.nome.asc()).paginate(page=page, per_page=per_page)

        if not clientes.items:
            flash("Nenhum registro encontrado", "danger")

    return render_template(
                          "search_client.html",
                          title="Pesquisar Clientes",
                          form=form, clientes=clientes,
                          opcao_busca=opcao_busca,
                          valor_busca=valor_busca)


@clientes.route('/view/client/<id>', methods=['GET'])
@login_required
def view_client(id):
    cliente = Cliente.query.get(id)
    oss = Os.query.filter_by(id_cliente=cliente.id).order_by(Os.data_entrada.desc()).paginate(page=1, per_page=10)
    return render_template('view_client.html', title="Dados do Cliente", cliente=cliente, oss=oss)

@clientes.route('/update/client/<id>', methods=['GET', 'POST'])
@login_required
def update_client(id):
    cliente = Cliente.query.get(id)
    form = UpdateClientForm()
    if form.validate_on_submit():
        cliente.telefone = form.phone.data
        cliente.celular = form.mobile.data
        cliente.email = form.email.data
        cliente.cep = form.cep.data
        cliente.cidade = form.city.data
        cliente.estado = form.state.data
        cliente.bairro = form.neighborhood.data
        cliente.endereco = form.address.data
        cliente.numero = form.number.data
        cliente.complemento = form.complement.data
        db.session.commit()
        flash('O cadastro foi atualizado com sucesso!', 'success')
        return redirect(url_for('clientes.view_client', id=id))
    elif request.method == 'GET':
        form.phone.data == cliente.telefone
        form.mobile.data == cliente.celular
        form.email.data == cliente.email
        form.cep.data == cliente.cep
        form.city.data == cliente.cidade
        form.state.data == cliente.estado
        form.neighborhood.data == cliente.bairro
        form.address.data == cliente.endereco
        form.number.data == cliente.numero
        form.complement.data == cliente.complemento
    return render_template('update_client.html', title="Alterar Dados do Cliente", form=form, cliente=cliente)

@clientes.route('/register/check', methods=['GET', 'POST'])
@login_required
def check_register_type():
    form = CheckCPFForm()
    if form.validate_on_submit():
        cliente = Cliente.query.filter_by(cpf=form.check_cpf_field.data).first()

        if cliente:
            return redirect(url_for('clientes.view_client', id=cliente.id))
        else:
            flash("Não há nenhum cliente registrado com este CPF.", "danger")

    return render_template('client_has_registry.html', title="Nova Ordem de Serviço", form=form)