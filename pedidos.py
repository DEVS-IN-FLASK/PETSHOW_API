from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Pedido
from petshow_api import db

pedidos_app = Blueprint('pedidos', __name__, url_prefix='/pedidos')

@pedidos_app.route('/')
def listar():
    profs = Pedido.query.all()
#    return jsonify([{"json de dados}])
    return jsonify([p.serialize() for p in profs])

@pedidos_app.route('/',methods=['POST'])
def novo():
    novo_pedido = request.get_json()
    if not novo_pedido:
        return jsonify({'erro':'Os dados do pedido não foram inseridos'})
    try:
        p = Pedido(nome=novo_pedido.get('nome'))
        db.session.add(p)
        db.session.commit()
        return jsonify(p.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Pedido já cadastrado"}),400