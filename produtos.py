from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Produto, Marca, Tamanho, Animal
from petshow_api import db

produtos_app = Blueprint('produtos', __name__,url_prefix='/produtos')

@produtos_app.route('/')
def listar():
    prod = Produto.query.all() #Necessário incluir na listagem tamanho, animal e marca
    return jsonify([p.serialize() for p in prod])

@produtos_app.route('/',methods=['POST'])
def novo():
    novo_produto = request.get_json()
    if not novo_produto:
        return jsonify({'erro':'Os dados do produto não foram inseridos'})
    try:
        
        t = Tamanho(id=novo_produto.get('id'),tamanho=novo_produto.get('tamanho'))
        a = Animal(id=novo_produto.get('id'),animal=novo_produto.get('animal'))
        m = Marca(id=novo_produto.get('id'),marca=novo_produto.get('marca'))

        p = Produto(descricao=novo_produto.get('descricao'),modelo=novo_produto.get('modelo'),
        cod_barras=novo_produto.get('cod_barras'), porcentagem=novo_produto.get('porcentagem'),
        preco_custo=novo_produto.get('preco_custo'), preco_venda=novo_produto.get('preco_venda'),foto=novo_produto.get('foto'))     
        
        db.session.add(t)
        db.session.add(a)    
        db.session.add(m)
        db.session.add(p)
        
        db.session.commit()
        return jsonify(p.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Produto já cadastrado"}),400