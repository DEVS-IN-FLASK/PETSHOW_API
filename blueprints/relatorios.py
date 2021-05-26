from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from models import Produto, Cliente, Usuario, Pedido, Pedido_Produto, Marca, Tamanho, Animal, Situacao
from petshow_api import db
from datetime import datetime

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

relatorios_app = Blueprint('relatorios', __name__,url_prefix='/relatorios')


# Rotas para consulta de relatórios

@relatorios_app.route('/')
@jwt_required()
def relatorios():
    if request.method == 'GET':
        try:
            data = request.args['data']
            data_inicial = datetime.strptime(data[0:10], '%d/%m/%Y')
            data_final = datetime.strptime(data[13:], '%d/%m/%Y')
            pedidos = db.session.query(Pedido.situacao_id, func.sum(Pedido_Produto.total), func.count(Pedido.situacao_id)).filter(Pedido_Produto.pedido_id == Pedido.id, Pedido.data > data_inicial, Pedido.data < data_final).group_by(Pedido.situacao_id).all()  
            lista = {'periodo': data,
                    'concluido': 0,
                    'recebido': 0,
                    'cancelado': 0,
                    'ticket_medio': 0}
            if pedidos != []:
                for x in pedidos:
                    if x[0] == 1:
                        lista['concluido'] = x[1]
                        lista['ticket_medio'] = x[1] / x[2]
                    elif x[0] == 2:
                        lista['recebido'] = x[1]
                    elif x[0] == 3:
                        lista['cancelado'] = x[1]
            return jsonify(lista)
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})

