from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models import Animal, Marca, Produto, Tamanho
from petshow_api import db

produtos_app = Blueprint('produtos', __name__,url_prefix='/produtos')


# Rotas para cadastro de produtos

@produtos_app.route('/',methods=['GET','POST'])
def produtos():
    if request.method == 'GET':
        try:
            produtos = Produto.query.all()
            return jsonify([produto.serialize() for produto in produtos])
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})
    elif request.method == 'POST':
        dados = request.get_json()
        if not dados:
            return jsonify({'erro':'Os dados do produto não foram inseridos'})
        try:
            produto = Produto(nome=dados['nome'],descricao=dados['descricao'], modelo=dados['modelo'],
            cod_barras=dados['cod_barras'], porcentagem=dados['porcentagem'],
            preco_custo=dados['preco_custo'], preco_venda=dados['preco_venda'], quantidade=dados['quantidade'],
            foto=dados['foto'], marca_id=dados['marca_id'], tamanho_id=dados['tamanho_id'], animal_id=dados['animal_id'], usuario_id=dados['usuario_id'])
            db.session.add(produto)
            db.session.commit()
            return jsonify({'sucesso':'Produto cadastrado'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'erro':"Produto já cadastrado"}),400
        except Exception:
            return jsonify({'Sistema':'Os dados do produto não foram inseridos'})

@produtos_app.route('/<id>/remover/', methods=['DELETE'])
def remover_produto(id):
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

@produtos_app.route('/<id>/alterar/', methods=['PUT'])
def alterar_produto(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Os dados do produto não foram inseridos'})
    try:
        produto = Produto(nome=dados['nome'],descricao=dados['descricao'], modelo=dados['modelo'],
            cod_barras=dados['cod_barras'], porcentagem=dados['porcentagem'],
            preco_custo=dados['preco_custo'], preco_venda=dados['preco_venda'], quantidade=dados['quantidade'], foto=dados['foto'], marca_id=dados['marca_id'], tamanho_id=dados['tamanho_id'], animal_id=dados['animal_id'])
        produto.nome = dados['nome']
        produto.descricao = dados['descricao']
        produto.modelo = modelo=dados['modelo']
        produto.cod_barras = cod_barras=dados['cod_barras']
        produto.porcentagem = porcentagem=dados['porcentagem']
        produto.preco_custo = preco_custo=dados['preco_custo']
        produto.preco_venda = preco_venda=dados['preco_venda']
        produto.quantidade = dados['quantidade']
        produto.foto = dados['foto']
        produto.marca_id = dados['marca_id']
        produto.tamanho_id = dados['tamanho_id']
        produto.animal_id = animal_id=dados['animal_id']
        db.session.commit()
        return jsonify({'sucesso':'Produto alterado'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})

# Rotas para cadastro de marcas

@produtos_app.route('/marcas/', methods=['GET', 'POST'])
def marcas():
    if request.method == 'GET':
        try:
            marcas = Marca.query.all()
            return jsonify([marca.serialize() for marca in marcas])
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})
    elif request.method == 'POST':
        try:
            dados = request.get_json()
            marca = Marca(marca=dados['marca'])
            db.session.add(marca)
            db.session.commit()
            return jsonify({'sucesso':"Marca cadastrada"})
        except IntegrityError:
            return jsonify({'erro':"Marca ja cadastrada"})
        except Exception:
            return jsonify({'erro':'Os dados da marca nao foram inseridos'})

@produtos_app.route('/marcas/<id>/remover/', methods=['DELETE'])
def remover_marca(id):
    try:
        marca = Marca.query.filter_by(id=id).first()
        if marca is not None:
            db.session.delete(marca)
            db.session.commit()
            return jsonify({'sucesso':'Marca removida'})
        else:
            return jsonify({'erro':'Produto nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})

# Rotas para cadastro de tamanhos

@produtos_app.route('/tamanhos/', methods=['GET', 'POST'])
def tamanhos():
    if request.method == 'GET':
        try:
            tamanhos = Tamanho.query.all()
            return jsonify([tamanho.serialize() for tamanho in tamanhos])
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})
    elif request.method == 'POST':
        try:
            dados = request.get_json()
            tamanho = Tamanho(tamanho=dados['tamanho'])
            db.session.add(tamanho)
            db.session.commit()
            return jsonify({'sucesso':"Tamanho cadastrado"})
        except IntegrityError:
            return jsonify({'erro':"Tamanho ja cadastrado"})
        except Exception:
            return jsonify({'erro':'Os dados de tamanho nao foram inseridos'})

@produtos_app.route('/tamanhos/<id>/remover/', methods=['DELETE'])
def remover_tamanho(id):
    try:
        tamanho = Tamanho.query.filter_by(id=id).first()
        if tamanho is not None:
            db.session.delete(tamanho)
            db.session.commit()
            return jsonify({'sucesso':'Tamanho removido'})
        else:
            return jsonify({'erro':'Tamanho nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})


# Rotas para cadastro de animais

@produtos_app.route('/animais/', methods=['GET', 'POST'])
def animais():
    if request.method == 'GET':
        try:
            animais = Animal.query.all()
            return jsonify([animal.serialize() for animal in animais])
        except Exception:
            return jsonify({'erro':"Nao foi possivel acessar os dados"})
    elif request.method == 'POST':
        try:
            dados = request.get_json()
            animal = Animal(animal=dados['animal'])
            db.session.add(animal)
            db.session.commit()
            return jsonify({'sucesso':"Animal cadastrado"})
        except IntegrityError:
            return jsonify({'erro':"Animal ja cadastrado"})
        except Exception:
            return jsonify({'erro':'Os dados de animal nao foram inseridos'})

@produtos_app.route('/animais/<id>/remover/', methods=['DELETE'])
def remover_animal(id):
    try:
        animal = Animal.query.filter_by(id=id).first()
        if animal is not None:
            db.session.delete(animal)
            db.session.commit()
            return jsonify({'sucesso':'Animal removido'})
        else:
            return jsonify({'erro':'Animal nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})
