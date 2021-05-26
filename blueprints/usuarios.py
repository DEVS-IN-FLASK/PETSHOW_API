from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from models import Usuario
from petshow_api import db
import datetime

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

usuarios_app = Blueprint('usuarios', __name__,url_prefix='/usuarios')

@usuarios_app.route('/',methods=['GET'])
@jwt_required()
def listar():
    try:
        current_user = get_jwt_identity()
        user = Usuario.query.all()
        return jsonify([u.serialize() for u in user])
    except Exception:
        return jsonify({'erro':'Nao foi possivel acessar os dados'})

@usuarios_app.route('/verificar/', methods=['GET'])
@jwt_required()
def verificar_token():
    return jsonify({'sucesso':'token valido'})
#se 'msg' aplicação principal deve levar o usuário para a tela de login

@usuarios_app.route('/<login>', methods=['GET'])
@jwt_required()
def usuario_por_login(login):
    try:
        user = Usuario.query.filter_by(login=login).first()
        if user is not None:
            return jsonify(user.serialize())
        else:
            return jsonify({'erro':'Usuario nao encontrado'})
    except Exception:
        return jsonify({'erro':'Nao foi possivel acessar os dados'})

@usuarios_app.route('/autenticar', methods=['POST'])
def autentica_usuario():
    dados_usuario = request.get_json()
    try:
        login = dados_usuario['login']
        senha = dados_usuario['senha']
        user = Usuario.query.filter_by(login=login).first()
        if user.tipo != 'inativo':
            if check_password_hash(user.senha, senha):
                access_token = create_access_token(identity=login, expires_delta=datetime.timedelta(minutes=30))
                return jsonify({'sucesso':'autenticado', 'access_token': access_token})
            else:
                return jsonify({'erro':"Usuario ou senha incorretos"})
        else:
            return jsonify({'erro':'Usuário inativo'})
    except Exception:
        return jsonify({'erro':"Usuario ou senha incorretos"})

@usuarios_app.route('/novo',methods=['POST'])
@jwt_required()
def novo():
    current_user = get_jwt_identity()
    user = Usuario.query.filter_by(login=current_user).first()
    if user.tipo == 'gerente':
        novo_usuario = request.get_json()
        if not novo_usuario:
            return jsonify({'erro':'Os dados do usuario não foram inseridos'})
        try:
            nome = novo_usuario.get('nome')
            senha = novo_usuario.get('senha')
            login = novo_usuario.get('login')
            if len(nome) < 4 or len(nome) > 30 or len(login) < 4 or len(login) > 15 or len(senha) < 5:
                raise Exception
            else:
                u = Usuario(login=login, nome=nome, senha=generate_password_hash(senha),tipo=novo_usuario.get('tipo'))
                db.session.add(u)
                db.session.commit()
                return jsonify({'sucesso':'Usuario cadastrado'})

        except IntegrityError:
            db.session.rollback()
            return jsonify({'erro':"Usuario já cadastrado"}),400
        except Exception:
            db.session.rollback()
            return jsonify({'erro':"Nao foi possivel cadastrar o usuario"})
    else:
        return jsonify({'erro':"Usuario nao habilitado"})

@usuarios_app.route('/alterarsenha',methods=['PATCH'])
@jwt_required()
def alterar_senha():
    dados_usuario = request.get_json()
    current_user = get_jwt_identity()
    user = Usuario.query.filter_by(login=current_user).first()
    if not dados_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        login = dados_usuario['login']
        senha = dados_usuario['senha']
        if user.login == login:
            user = Usuario.query.filter_by(login=login).first()
            user.senha = generate_password_hash(senha)
            db.session.commit()
            return jsonify({'sucesso':'Senha alterada'})
        else:
            return jsonify({'erro':"Usuario nao habilitado"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400
    except Exception:
            db.session.rollout()
            return jsonify({'erro':"Nao foi possivel alterar o usuario"})

@usuarios_app.route('/alterartipo',methods=['PATCH'])
@jwt_required()
def alterar_tipo():
    dados_usuario = request.get_json()
    current_user = get_jwt_identity()
    user = Usuario.query.filter_by(login=current_user).first()
    if user.tipo == 'gerente':
        if not dados_usuario:
            return jsonify({'erro':'Os dados do usuario não foram inseridos'})
        try:
            login = dados_usuario['login']
            tipo = dados_usuario['tipo']
            if login != 'admin':
                user = Usuario.query.filter_by(login=login).first()
                user.tipo = tipo
                db.session.commit()
                return jsonify({'sucesso':'Tipo alterado'})
            else:
                return jsonify({'erro':'Nao e possivel alterar o usuario admin'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'erro':"Nao foi possivel fazer a alteracao"}),400
    else:
        return jsonify({'erro':"Usuario nao habilitado"})

'''
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
'''