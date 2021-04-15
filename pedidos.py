from flask import Blueprint, jsonify, request
from flask.globals import session
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy

from models import Pedido
from petshow_api import db

pedidos_app = Blueprint('pedidos', __name__,url_prefix='/pedidos')


# Rotas para cadastro de pedidos

@pedidos_app.route('/',methods=['GET','POST'])
def pedidos():
    if request.method == 'GET':
        try:
            pedidos = Pedido.query.all()
            return jsonify([pedido.serialize() for pedido in pedidos])
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})
    elif request.method == 'POST':
        dados = request.get_json()
        if not dados:
            return jsonify({'erro':'Os dados do pedido não foram inseridos'})
        try:
            pedido = Pedido(data=dados['data'],observacao=dados['observacao'], quantidade=dados['quantidade'],
            preco=dados['preco'], total=dados['total'],
            usuario_id=dados['usuario_id'], cliente_id=dados['cliente_id'], situacao_id=dados['situacao_id'])

            db.session.add(pedido)
            db.session.commit()
            return jsonify({'sucesso':'Pedido cadastrado'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'erro':"Pedido já cadastrado"}),400
        except Exception:
            return jsonify({'Sistema':'Os dados do pedido não foram inseridos'})

@pedidos_app.route('/<id>/remover/', methods=['DELETE'])
def remover_pedido(id):
    try:
        pedido = Pedido.query.filter_by(id=id).first()
        if pedido is not None:
            db.session.delete(pedido)
            db.session.commit()
            return jsonify({'sucesso':'Pedido removido'})
        else:
            return jsonify({'erro':'Pedido nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})

@pedidos_app.route('/<id>/alterar/', methods=['PUT'])
def alterar_pedido(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Os dados do produto não foram inseridos'})
    try:
        pedido = Pedido(data=dados['data'],observacao=dados['observacao'], quantidade=dados['quantidade'],
            preco=dados['preco'], total=dados['total'],
            usuario_id=dados['usuario_id'], cliente_id=dados['cliente_id'], situacao_id=dados['situacao_id'])
        pedido.data = dados['nome']
        pedido.observacao = dados['descricao']
        pedido.quantidade = modelo=dados['modelo']
        pedido.preco = cod_barras=dados['cod_barras']
        pedido.cliente_id = porcentagem=dados['porcentagem']
        pedido.situacao_id = preco_custo=dados['preco_custo']
  
        db.session.commit()
        return jsonify({'sucesso':'Pedido alterado'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})



