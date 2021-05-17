from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Produto, Cliente, Usuario, Pedido, Pedido_Produto, Marca, Tamanho, Animal, Situacao
from petshow_api import db
from datetime import datetime

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

pedidos_app = Blueprint('pedidos', __name__,url_prefix='/pedidos')


# Rotas para cadastro de pedidos

@pedidos_app.route('/',methods=['GET','POST'])
@jwt_required()
def pedidos():
    if request.method == 'GET':
        try:
            pedidos = Pedido.query.all()
            lista = {'pedidos':[]}
            for x in pedidos:
                cliente = Cliente.query.filter_by(id=x.cliente_id).first()
                item = {}
                item['pedido'] = x.serialize()
                item['situacao'] = Situacao.query.filter_by(id=x.situacao_id).first().descricao
                item['cliente'] = cliente.serialize()
                item['itens'] = []
                itens = Pedido_Produto.query.filter_by(pedido_id=x.id).all()
                for y in itens:
                    item['itens'].append(y.serialize())
                lista['pedidos'].append(item)
            return jsonify(lista)
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})

    elif request.method == 'POST':
        dados = request.get_json()
        if not dados:
            return jsonify({'erro':'Os dados do pedido não foram inseridos'})
        try:
#            current_user = get_jwt_identity()
#            user_id = Usuario.query.filter_by(login=login).first().id

            pedido = Pedido(cliente_id=dados['cliente_id'], usuario_id=dados['usuario_id'], observacao=dados['observacao'],
                            situacao_id=1, data=datetime.utcnow())  
            db.session.add(pedido)
            db.session.commit()
            pedido_id = pedido.id
            itens = dados['itens']
            for item in itens:
                preco = Produto.query.filter_by(id=item['produto_id']).first().preco_venda
                total = preco * item['quantidade']
                pedido_produto = Pedido_Produto(produto_id=item['produto_id'], quantidade=item['quantidade'], pedido_id=pedido_id, preco=preco, total=total)
                db.session.add(pedido_produto)
            db.session.commit()
            return jsonify({'sucesso':'Pedido cadastrado'})
        except Exception as e:
            print(e)
            return jsonify({'erro':'Os dados do pedido nao puderam ser inseridos'})

@pedidos_app.route('/<id>/situacao/', methods=['PUT'])
@jwt_required()
def alterar_situacao(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Os dados do pedido não foram inseridos'})
    try:
        situacao = dados['situacao_id']
        pedido = Pedido.query.filter_by(id=id).first()
        pedido.observacao = dados['observacao']
        db.session.commit()
        situacao_atual = pedido.situacao_id
        if situacao == 1:
            pedido.situacao_id = situacao
            db.session.commit()
            return jsonify({'sucesso':'Pedido alterado'})
        if situacao == 2:
            itens = db.session.query(Pedido_Produto, Produto).filter(Pedido_Produto.produto_id == Produto.id, Pedido_Produto.pedido_id == id).all()
            for item in itens:
                if item.Produto.quantidade >= item.Pedido_Produto.quantidade:
                    item.Produto.quantidade -= item.Pedido_Produto.quantidade
                else:
                    raise ValueError('Quantidade insuficiente de produto em estoque')
            db.session.commit()
            pedido.situacao_id = situacao
            db.session.commit()
            return jsonify({'sucesso':'Pedido concluido'})
        elif situacao == 3:
            itens = db.session.query(Pedido_Produto, Produto).filter(Pedido_Produto.produto_id == Produto.id, Pedido_Produto.pedido_id == id).all()
            if situacao_atual == 2:
                for item in itens:
                    item.Produto.quantidade += item.Pedido_Produto.quantidade
                db.session.commit()
            pedido.situacao_id = situacao
            db.session.commit()
            return jsonify({'sucesso':'Pedido cancelado'})
    except ValueError as e:
        return jsonify({'erro':e.args})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})

@pedidos_app.route('/<id>/itens/', methods=['PUT'])
@jwt_required()
def alterar_itens(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Os dados do pedido não foram inseridos'})
    try:
        situacao = Pedido.query.filter_by(id=id).first().situacao_id
        itens = Pedido_Produto.query.filter_by(pedido_id=id).all()
        novos = dados['itens']
        if situacao == 1:
            for item in itens:
                db.session.delete(item)
            db.session.commit()
            for item in novos:
                preco = Produto.query.filter_by(id=item['produto_id']).first().preco_venda
                total = preco * item['quantidade']
                novo = Pedido_Produto(produto_id=item['produto_id'], pedido_id=id, quantidade=item['quantidade'], preco=preco, total=total)
                db.session.add(novo)
            db.session.commit()
            return jsonify({'sucesso':'Pedido alterado'})
        else:
            raise ValueError('Pedido nao pode ser alterado')
    except ValueError as e:
        return jsonify({'erro':e.args})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})

