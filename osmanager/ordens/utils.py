from osmanager.models import Os, Cliente
from osmanager import db

def busca_os(parametro, valor_busca, page, per_page):
    clientes = []
    tem_registro = True
    
    if parametro == "cpf":    
        cliente = Cliente.query.filter_by(cpf=valor_busca).first()
        if cliente:
            oss = Os.query.filter_by(id_cliente=cliente.id).order_by(Os.data_entrada.desc()).paginate(page=page, per_page=per_page)
            for os in oss.items:
                clientes.append(Cliente.query.get(os.id_cliente))
        else:
            oss = None
            tem_registro = False
    elif parametro == "status":
        oss = Os.query.filter(f"LOWER(status) = LOWER('{valor_busca}')").order_by(Os.data_entrada.desc()).paginate(page=page, per_page=per_page)
        if not oss.items:
            tem_registro = False
        else:
            for os in oss.items:
                clientes.append(Cliente.query.get(os.id_cliente))
    elif parametro == 'numero_os':
        oss = Os.query.filter(db.text(f"numero = {valor_busca}")).order_by(Os.numero.asc()).paginate(page=page, per_page=per_page)
        if not oss.items:
            tem_registro = False
        else:
            for os in oss.items:
                clientes.append(Cliente.query.get(os.id_cliente))
    else:
        oss = Os.query.order_by(Os.data_entrada.desc()).paginate(page=page, per_page=per_page)
        for os in oss.items:
            clientes.append(Cliente.query.filter_by(id=os.id_cliente).first())
    return {'oss': oss,
            'clientes': clientes,
            'tem_registro': tem_registro}