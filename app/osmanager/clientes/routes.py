from flask import render_template, url_for, flash, redirect, request, Blueprint
from osmanager import db
from osmanager.clientes.forms import ClientForm, SearchClientForm, CheckCPFForm
from osmanager.models import Cliente
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
    return render_template('view_client.html', title="Dados do Cliente", cliente=cliente)

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