from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Usuario
from pet import db

usuarios_app = Blueprint('usuarios', __name__,url_prefix='/usuarios')

@usuarios_app.route('/')
def listar():
    user = Usuario.query.all()
#    return jsonify([{"id":1, "nome":"Gerson"}])
    return jsonify([p.serialize() for p in user])

@usuarios_app.route('/',methods=['POST'])
def novo():
    novo_usuario = request.get_json()
    if not novo_usuario:
        return jsonify({'erro':'Os dados do usuario não foram inseridos'})
    try:
        u = Usuario(login=novo_usuario.get('login'), nome=novo_usuario.get('nome'), senha=novo_usuario.get('senha'))
        db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro':"Usuario já cadastrado"}),400