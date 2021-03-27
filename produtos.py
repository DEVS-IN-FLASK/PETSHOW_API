from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models import Animal, Marca, Produto, Tamanho
from petshow_api import db

produtos_app = Blueprint('produtos', __name__,url_prefix='/produtos')

@produtos_app.route('/')
def listar():
    prod = Produto.query.all()
    return jsonify([p.serialize() for p in prod])

@produtos_app.route('/',methods=['POST'])
def novo():
    novo_produto = request.get_json()
    if not novo_produto:
        return jsonify({'erro':'Os dados do produto não foram inseridos'})
    try:
        
        t = Tamanho(tamanho=novo_produto.get('tamanho'))
        a = Animal(animal=novo_produto.get('animal'))
        m = Marca(marca=novo_produto.get('marca'))
        
        p = Produto(descricao=novo_produto.get('descricao'),modelo=novo_produto.get('modelo'),
        cod_barras=novo_produto.get('cod_barras'), porcentagem=novo_produto.get('porcentagem'),
        preco_custo=novo_produto.get('preco_custo'), preco_venda=novo_produto.get('preco_venda'),foto=novo_produto.get('foto'),marca = m, tamanho = t, animal=a) 

        
        db.session.add(p)
        db.session.commit()
        return jsonify(p.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Produto já cadastrado"}),400

@produtos_app.route('/<id>/remover', methods=['DELETE'])
def remover_usuario(id):
    try:
        produto = Produto.query.filter_by(id=id).first()
        if produto is not None:
            db.session.delete(produto)
            db.session.commit()
            return jsonify({'sucesso':'Produto removido'})
        else:
            return jsonify({'erro':'Produto nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})
