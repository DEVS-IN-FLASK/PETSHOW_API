from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Cliente, Endereco
from petshow_api import db

clientes_app = Blueprint('clientes', __name__,url_prefix='/clientes')

@clientes_app.route('/')
def listar():
    cli = Cliente.query.all()

    return jsonify([c.serialize() for c in cli])

@clientes_app.route('/',methods=['POST'])
def novo():
    novo_cliente = request.get_json()
    if not novo_cliente:
        return jsonify({'erro':'Os dados do cliente não foram inseridos'})
    try:
        c = Cliente(nome=novo_cliente.get('nome'), email=novo_cliente.get('email'), cpf=novo_cliente.get('cpf'), 
        rua=novo_cliente.get('rua'), cep=novo_cliente.get('cep'), bairro=novo_cliente.get('bairro'), cidade=novo_cliente.get('cidade'), uf=novo_cliente.get('uf'))
        db.session.add(c)
        db.session.commit()
        return jsonify(c.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Cliente já cadastrado"}),400