from models.marca import Marca
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Produto, Marca
from petshow_api import db

produtos_app = Blueprint('produtos', __name__,url_prefix='/produtos')

@produtos_app.route('/')
def listar():
    prod = Produto.query.all()
#    return jsonify([{"id":1, "nome":"Gerson"}])
    return jsonify([p.serialize() for p in prod])

@produtos_app.route('/',methods=['POST'])
def novo():
    novo_produto = request.get_json()
    if not novo_produto:
        return jsonify({'erro':'Os dados do produto não foram inseridos'})
    try:


        p = Produto(descricao=novo_produto.get('descricao'),modelo=novo_produto.get('modelo'),
            cod_barras=novo_produto.get('cod_barras'), porcentagem=novo_produto.get('porcentagem'),
            preco_custo=novo_produto.get('preco_custo'), preco_venda=novo_produto.get('preco_venda'),foto=novo_produto.get('foto'),marcas_id=novo_produto.get('marcas_id'))

        m = Marca(id=novo_produto.get('id'),marca=novo_produto.get('marca'))
            
#        p.append(m)
        db.session.add(p,m)  
        db.session.commit()
        return jsonify(p.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Produto já cadastrado"}),400