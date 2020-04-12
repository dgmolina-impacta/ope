from flask import render_template, url_for, flash, redirect, request
from osmanager import app, db, bcrypt
from osmanager.forms import RegistrationForm, LoginForm, UpdateAccountForm, ClientForm, SearchClientForm, NewSOForm, SearchSOForm, AddComponentForm, FullRegisterForm
from osmanager.models import User, Cliente, Os, Equipamento, Peca
from flask_login import login_user, current_user, logout_user, login_required

os = {"numero": "xxxxx",
    "cliente": "Daniel Gomes Molina",
    "equipamento": "Balança Filizola",
    "status": "Em manutenção"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", os=os)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sua conta foi criada!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Por Favor verifique seu email e a senha', 'danger')
    return render_template("login.html", title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Sua conta foi atualizada!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        print(f"{form.username.data} and {form.email.data}")
    return render_template("account.html", title='Account', form=form)


@app.route('/register/client', methods=['GET', 'POST'])
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
        return redirect(url_for("home"))
    return render_template("client.html", title='Novo Cliente', form=form)


@app.route('/search/client', methods=['GET', 'POST'])
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


@app.route('/view/client/<id>', methods=['GET'])
@login_required
def view_client(id):
    cliente = Cliente.query.get(id)
    return render_template('view_client.html', title="Dados do Cliente", cliente=cliente)


@app.route('/register/check', methods=['GET'])
@login_required
def check_register_type():
    return render_template('client_has_registry.html', title="Nova Ordem de Serviço")


@app.route('/register/all', methods=['GET', 'POST'])
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
        return redirect(url_for("home"))
    return render_template('full_register.html', title="Cadastro Completo", form=form)

@app.route('/register/so/<id>', methods=['GET', 'POST'])
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
        return redirect(url_for("home"))
    return render_template("new_so.html", title='Novo Ordem de Serviço', form=form)


@app.route('/search/so', methods=['GET', 'POST'])
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


@app.route('/view/so/<numero>', methods=["GET", "POST"])
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


