from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from models import Usuario
from petshow_api import db

usuarios_app = Blueprint('usuarios', __name__,url_prefix='/usuarios')

@usuarios_app.route('/',methods=['GET'])
def listar():
    try:
        user = Usuario.query.all()
        return jsonify([u.serialize() for u in user])
    except Exception:
        return jsonify({'erro':'Nao foi possivel acessar os dados'})

@usuarios_app.route('/<login>', methods=['GET'])
def usuario_por_login(login):
    try:
        user = Usuario.query.filter_by(login=login).first()
        if user is not None:
            return jsonify(user.serialize())
        else:
            return jsonify({'erro':'Usuario nao encontrado'})
    except Exception:
        return jsonify({'erro':'Nao foi possivel acessar os dados'})

@usuarios_app.route('/autenticar', methods=['GET'])
def autentica_usuario():
    dados_usuario = request.get_json()
    try:
        login = dados_usuario['login']
        senha = dados_usuario['senha']
        user = Usuario.query.filter_by(login=login).first()
        if check_password_hash(user.senha, senha):
            return jsonify({'sucesso':'Usuario autenticado'})
        else:
            return jsonify({'erro':"Usuario ou senha incorretos"})
    except Exception:
        return jsonify({'erro':"Usuario ou senha incorretos"})

@usuarios_app.route('/novo',methods=['POST'])
def novo():
    novo_usuario = request.get_json()

    if not novo_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        u = Usuario(login=novo_usuario.get('login'), nome=novo_usuario.get('nome'), email=novo_usuario.get('email'),senha=generate_password_hash(novo_usuario.get('senha')),tipo=novo_usuario.get('tipo'))
        db.session.add(u)
        db.session.commit()
        return jsonify({'sucesso':'Usuario cadastrado'})

    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Usuario já cadastrado"}),400

@usuarios_app.route('/alterarsenha',methods=['PATCH'])
def alterar_senha():
    dados_usuario = request.get_json()

    if not dados_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        login = dados_usuario['login']
        senha = dados_usuario['senha']
        user = Usuario.query.filter_by(login=login).first()
        user.senha = generate_password_hash(senha)
        db.session.commit()
        return jsonify({'sucesso':'Senha alterada'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400

@usuarios_app.route('/alterartipo',methods=['PATCH'])
def alterar_tipo():
    dados_usuario = request.get_json()

    if not dados_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        login = dados_usuario['login']
        tipo = dados_usuario['tipo']
        user = Usuario.query.filter_by(login=login).first()
        user.tipo = tipo
        db.session.commit()
        return jsonify({'sucesso':'Tipo alterada'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400

@usuarios_app.route('/<login>/remover', methods=['DELETE'])
def remover_usuario(login):
    try:
        user = Usuario.query.filter_by(login=login).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'sucesso':'Usuario removido'})
        else:
            return jsonify({'erro':'Usuario nao encontrado'})
    except Exception:
        return jsonify({'erro':"Nao foi possivel acessar os dados"})
