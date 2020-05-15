from flask import render_template, url_for, flash, redirect, request, Blueprint
from osmanager import db
from osmanager.ordens.forms import NewSOForm, SearchSOForm, AddComponentForm, FullRegisterForm
from osmanager.models import Cliente, Os, Equipamento, Peca
from flask_login import login_required


ordens = Blueprint('ordens', __name__)

@ordens.route('/register/so/<id>', methods=['GET', 'POST'])
@login_required
def register_so(id):
    cliente = Cliente.query.get(id)
    form = NewSOForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("Validou")
        registro_equipamento = Equipamento(nro_de_serie=form.nro_de_serie.data,
                                           capacidade=form.capacidade.data,
                                           lacre_entrada=form.lacre_entrada.data,
                                           marca=form.marca.data,
                                           modelo=form.modelo.data
                                           )
        registro_os = Os(data_entrada=form.data_entrada.data,
                         tipo_defeito=form.tipo_defeito.data,
                         status=form.status.data,
                         problema_informado=form.problema_informado.data,
                         )
        registro_os.equipamento = registro_equipamento
        cliente.oss.append(registro_os)
        db.session.commit()
        flash("Ordem de serviço registrada com sucesso", "success")
        return redirect(url_for("main.home"))
    return render_template("new_so.html", title='Novo Ordem de Serviço', form=form)


@ordens.route('/search/so', methods=['GET', 'POST'])
@login_required
def search_so():
    form = SearchSOForm()
    page = request.args.get("page", 1, type=int)
    per_page = 2
    clientes = []

    if form.validate_on_submit():
        opcao_busca = form.opcao_busca.data
        valor_busca = form.valor_busca.data
        page = 1 # reseta numero da pagina ao pesquisar
    else:
        opcao_busca = request.args.get("opcao_busca", None, type=str)
        valor_busca = request.args.get("valor_busca", None, type=str)

    if not (opcao_busca or valor_busca):
        oss = Os.query.order_by(Os.numero.asc()).paginate(page=page, per_page=per_page)
        for os in oss.items:
            clientes.append(Cliente.query.filter_by(id=os.id_cliente).first())
    else:
        if opcao_busca == "cpf":    
            cliente = Cliente.query.filter_by(cpf=valor_busca).first()
            oss = Os.query.filter_by(id_cliente=cliente.id).order_by(Os.numero.asc()).paginate(page=page, per_page=per_page)
            for os in oss.items:
                clientes.append(Cliente.query.get(os.id_cliente))
        else:
            oss = Os.query.filter(db.text(f"numero LIKE '%{valor_busca}%'")).order_by(Os.numero.asc()).paginate(page=page, per_page=per_page)
            for os in oss.items:
                clientes.append(Cliente.query.get(os.id_cliente))

        if not oss.items:
            flash("Nenhum registro encontrado", "danger")

    return render_template(
                          "search_so.html",
                          title="Pesquisar Clientes",
                          form=form, oss=oss,
                          clientes=clientes,
                          opcao_busca=opcao_busca,
                          valor_busca=valor_busca)


@ordens.route('/view/so/<numero>', methods=["GET", "POST"])
def view_so(numero):
    os = Os.query.get(numero)
    orcamento = os.orcamento
    equipamento = os.equipamento
    pecas = os.pecas
    cliente = Cliente.query.get(os.id_cliente)
    form = AddComponentForm()

    if form.validate_on_submit():
        peca = Peca(marca=form.marca.data, nome=form.nome.data, valor_unitario=form.valor_unitario.data, quantidade=form.quantidade.data, numero=len(pecas)+1, numero_os=os.numero)
        os.pecas.append(peca)
        db.session.commit()
        flash("Itens adicionados com sucessos", "success")
    elif form.is_submitted():
        flash("Erro ao adicionar itens à Ordem de Serviço", "danger")
    return render_template('view_so.html', title="Ordem de Serviço", os=os, cliente=cliente, equipamento=equipamento, pecas=pecas, orcamento=orcamento, form=form)

@ordens.route('/register/all', methods=['GET', 'POST'])
@login_required
def full_register():
    form = FullRegisterForm()
    
    if form.validate_on_submit():
        registro_cliente = Cliente(cpf=form.cpf.data, nome=form.name.data, 
                                telefone=form.phone.data, 
                                celular=form.mobile.data, email=form.email.data,
                                cep=form.cep.data, endereco=form.address.data,
                                numero=form.number.data, complemento=form.complement.data,
                                bairro=form.neighborhood.data, cidade=form.city.data,
                                estado=form.state.data
                                )
        registro_equipamento = Equipamento(nro_de_serie=form.nro_de_serie.data,
                                        capacidade=form.capacidade.data,
                                        lacre_entrada=form.lacre_entrada.data,
                                        marca=form.marca.data,
                                        modelo=form.modelo.data
                                        )
        registro_os = Os(data_entrada=form.data_entrada.data,
                        tipo_defeito=form.tipo_defeito.data,
                        status=form.status.data,
                        problema_informado=form.problema_informado.data,
                        )
        registro_os.equipamento = registro_equipamento
        registro_cliente.oss.append(registro_os)
        db.session.add(registro_cliente)
        db.session.commit()
        flash("Registro realizado com sucesso", "success")
        return redirect(url_for("main.home"))
    return render_template('full_register.html', title="Cadastro Completo", form=form)
