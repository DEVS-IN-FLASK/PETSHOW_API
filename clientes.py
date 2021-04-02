from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Cliente, Telefone, Endereco, Pet
from petshow_api import db
from sqlalchemy import select

clientes_app = Blueprint('clientes', __name__,url_prefix='/clientes')

@clientes_app.route('/')
def listar():
#    cli = select(Cliente, Endereco).join(Cliente.enderecos).order_by(Cliente.id, Endereco.id)
    cli = Cliente.query.all()
    return jsonify([c.serialize() for c in cli])
#    cli.append.Endereco.query.all() #Necessário incluir na listagem demais tabelas

@clientes_app.route('/',methods=['POST'])
def novo():
    novo_cliente = request.get_json()
    if not novo_cliente:
        return jsonify({'erro':'Os dados do cliente não foram inseridos'})
    try:
        
    #    t = Telefone(id=novo_cliente.get('id'),telefone=novo_cliente.get('telefone'))
        e = Endereco(id=novo_cliente.get('id'),rua=novo_cliente.get('rua'),cep=novo_cliente.get('cep'),bairro=novo_cliente.get('bairro'),cidade=novo_cliente.get('cidade'),uf=novo_cliente.get('uf'))
        c = Cliente(nome=novo_cliente.get('nome'),email=novo_cliente.get('email'),cpf=novo_cliente.get('cpf'),endereco = e)

        db.session.add(c)
        
        db.session.commit()
        return jsonify(c.serialize()) #precisa incluir as demais tabelas no retorno
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Cliente já cadastrado"}),400

