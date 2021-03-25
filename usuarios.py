from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Usuario
from petshow_api import db

usuarios_app = Blueprint('usuarios', __name__,url_prefix='/usuarios')

@usuarios_app.route('/')
def listar():
    user = Usuario.query.all()
    return jsonify([u.serialize() for u in user])

@usuarios_app.route('/',methods=['POST'])
def novo():
    novo_usuario = request.get_json()
    
    if not novo_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        u = Usuario(login=novo_usuario.get('login'), nome=novo_usuario.get('nome'), senha=novo_usuario.get('senha'),tipo=novo_usuario.get('tipo'))
        db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize())

    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Usuario já cadastrado"}),400