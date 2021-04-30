from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Pedido_Produto
from petshow_api import db

pedidos_app = Blueprint('pedidos', __name__, url_prefix='/pedidos')

@pedidos_app.route('/')
def listar():
    ped = Pedido_Produto.query.all()
#    return jsonify([{"json de dados}])
    return jsonify([p.serialize() for p in ped])

@pedidos_app.route('/novo',methods=['POST'])
def novo():
    novo_pedido = request.get_json()
    if not novo_pedido:
        return jsonify({'erro':'Os dados do pedido não foram inseridos'})
    try:
        p = jsonify([{"json de dados":"Wed Apr 21 2021 01:10:20 GMT-0300 (Horário Padrão de Brasília)","observacao":"obs","situacao":1,"usuario_id":3,"cliente_id":1}])
        
        #Pedido_Produto(observacao=novo_pedido.get('observacao'),situacao=novo_pedido.get('situacao'),
        #    situacao_id=novo_pedido.get('situacao_id'),usuario_id=novo_pedido.get('usuario_id'),cliente_id=novo_pedido.get('cliente_id'))
        db.session.add(p)
        db.session.commit()
        return jsonify(p.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Pedido já cadastrado"}),400