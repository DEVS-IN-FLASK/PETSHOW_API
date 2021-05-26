from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Cliente, Telefone, Endereco, Pet, Pets_Has_Clientes, Animal
from petshow_api import db

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

clientes_app = Blueprint('clientes', __name__,url_prefix='/clientes')

# inclusão e consulta de clientes e pets

@clientes_app.route('/pets/')
@jwt_required()
def pets():
    try:
        pets = Pet.query.all()
        return jsonify([p.serialize() for p in pets])
    except Exception:
        return jsonify({'erro':'Nao foi possivel acessar os dados'})
    
@clientes_app.route('/',methods=['GET', 'POST'])
@jwt_required()
def clientes():
    number_animais = len(Animal.query.all())
    if number_animais < 2:
        db.session.add(Animal(animal='cachorro'))
        db.session.add(Animal(animal='gato'))
        db.session.commit()
    if request.method == 'POST':
        dados = request.get_json()
        if not dados:
            return jsonify({'erro':'Os dados do cliente não foram inseridos'})
        try:    
            end = dados['endereco']
            endereco = Endereco(rua=end['rua'], numero=end['numero'], bairro=end['bairro'], cep=end['cep'], cidade=end['cidade'], uf=end['uf'])
            db.session.add(endereco)
            db.session.commit()
            end_id = endereco.id

            try:
                cliente = Cliente(nome=dados['nome'], email=dados['email'], cpf=dados['cpf'], endereco_id=end_id)
                if len(cliente.nome) < 4 :
                    raise Exception
                else:
                    db.session.add(cliente)
                    db.session.commit()
                    cli_id = cliente.id

                try:
                    tels = dados['telefones']
                    if (len(tels) > 0):
                        for tel in tels:
                            telefone = Telefone(telefone=tel['telefone'], cliente_id=cli_id)
                            db.session.add(telefone)
                            db.session.commit()
                except Exception:
                    db.session.rollback()
                    return jsonify({'erro':'Nao foi possivel cadastrar o telefone'})
                except IntegrityError:
                    db.session.rollback()
                    return jsonify({'erro':'Nao foi possivel cadastrar o telefone'})

                try:
                    pet_ids = []
                    pets = dados['pets']
                    if (len(pets) > 0):
                        for pt in pets:
                            busca_pet = Pet.query.filter_by(nome=pt['nome'], raca=pt['raca'], porte=pt['porte'], genero=pt['genero'], animal_id=pt['animal_id']).first()
                            if busca_pet is not None:
                                pet_ids.append(busca_pet.id)
                            else:
                                pet = Pet(nome=pt['nome'], raca=pt['raca'], porte=pt['porte'], genero=pt['genero'], animal_id=pt['animal_id'])
                                db.session.add(pet)
                                db.session.commit()
                                pet_ids.append(pet.id)
                        try:
                            for pet_id in pet_ids:
                                busca_rel = Pets_Has_Clientes.query.filter_by(cliente_id=cli_id, pet_id=pet_id).first()
                                if busca_rel is None:
                                    pets_has_clientes = Pets_Has_Clientes(cliente_id=cli_id, pet_id=pet_id)
                                    db.session.add(pets_has_clientes)
                                    db.session.commit()
                        except Exception:
                            db.session.rollback()
                            return jsonify({'erro':'Nao foi possivel cadastrar o relacionamento pet-cliente'})

                except Exception:
                    db.session.rollback()
                    return jsonify({'erro':'Nao foi possivel cadastrar o pet'})
                except IntegrityError:
                    db.session.rollback()
                    return jsonify({'erro':'Nao foi possivel cadastrar o pet'})

            except Exception:
                db.session.rollback()
                return jsonify({'erro':'Nao foi possivel cadastrar o cliente'})
            except IntegrityError:
                db.session.rollback()
                return jsonify({'erro':'Nao foi possivel cadastrar o cliente'})

            return jsonify({'sucesso':'Cliente cadastrado'})

        except Exception:
            db.session.rollback()
            return jsonify({'erro':'Nao foi possivel cadastrar o endereco'})

    elif request.method == 'GET':
        lista = dict()
        lista['clientes'] = []
        try:
            result = Cliente.query.outerjoin(Pets_Has_Clientes).all()
            result_tel = Telefone.query.all()
            for x in result:
                item_cliente = dict()
                item_cliente['cliente'] = x.serialize()
                item_cliente['cliente']['pets'] = []
                item_cliente['cliente']['telefones'] = []
                for pet in x.pets:
                    item_cliente['cliente']['pets'].append(pet.serialize())
                for tel in result_tel:
                    if tel.cliente_id == x.id:
                        item_cliente['cliente']['telefones'].append(tel.serialize())
                lista['clientes'].append(item_cliente)
            return lista
        except Exception:
            return jsonify({'erro':'Nao foi possivel acessar os dados'})

'''
# remocao de cliente, telefone, endereco e relacionamento com pet
# Não recomendável excluir um cliente - seguir o mesmo princípio do usuário, mantendo-o na base
@clientes_app.route('/<id>/remover/', methods=['DELETE'])
def remover_cliente(id):
    try:
        cliente = Cliente.query.filter_by(id=id).first()
        if cliente is not None:
            endereco = Endereco.query.filter_by(id=cliente.endereco_id).first()
            db.session.delete(endereco)
            telefones = Telefone.query.filter_by(cliente_id=cliente.id).all()
            for tel in telefones:
                db.session.delete(tel)
            pets_has_clientes = Pets_Has_Clientes.query.filter_by(cliente_id=cliente.id).all()
            for rel in pets_has_clientes:
                db.session.delete(rel)
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({'sucesso':'Cliente removido'})
        else:
            return jsonify({'erro':'Cliente nao encontrado'})
    except Exception:
        db.session.rollback()
        return jsonify({'erro':'Nao foi possivel acessar os dados'})
'''

@clientes_app.route('/<id>/alterar/', methods=['PUT'])
@jwt_required()
def alterar_cliente(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Os dados do cliente não foram inseridos'})
    try:
        cliente = Cliente.query.filter_by(id=id).first()
        if cliente is not None:
            cliente.nome = dados['nome']
            cliente.cpf = dados['cpf']
            cliente.email = dados['email']

            end = dados['endereco']
            endereco = Endereco.query.filter_by(id=cliente.endereco_id).first()
            endereco.rua = end['rua']
            endereco.numero = end['numero']
            endereco.bairro = end['bairro']
            endereco.cep = end['cep']
            endereco.cidade = end['cidade']
            endereco.uf = end['uf']

            lista_tel = dados['telefones']
            lista_tel_numeros = [x['telefone'] for x in lista_tel]
            db_tel = Telefone.query.filter_by(cliente_id=cliente.id).all()
            db_tel_numeros = [x.telefone for x in db_tel]
            
            for tel in lista_tel:
                if tel['telefone'] not in db_tel_numeros:
                    numero = Telefone(telefone=tel['telefone'], cliente_id=cliente.id)
                    db.session.add(numero)
            for tel in db_tel:
                if tel.telefone not in lista_tel_numeros:
                    db.session.delete(tel)
            
            lista_pet = dados['pets']
            lista_pet_index = [int(x['id']) for x in lista_pet if x != '']
            db_pet_has_clientes = Pets_Has_Clientes.query.filter_by(cliente_id=cliente.id).all()
            db_pet_index = [x.pet_id for x in db_pet_has_clientes]
            db_pet = [Pet.query.filter_by(id=x).one() for x in db_pet_index]
            
            
            for pet in lista_pet:
                if 'id' in pet:
                    if int(pet['id']) == 0:
                        new_pet = Pet(nome=pet['nome'], raca=pet['raca'], porte=pet['porte'], genero=pet['genero'], animal_id=pet['animal_id'])
                        db.session.add(new_pet)
                        db.session.commit()
                        new_pet_id = new_pet.id
                        pets_has_clientes = Pets_Has_Clientes(cliente_id=id, pet_id=new_pet_id)
                        db.session.add(pets_has_clientes)
                        db.session.commit()
                        lista_pet_index.append(new_pet_id)
                    else:
                        if int(pet['id']) not in db_pet_index:
                            pets_has_clientes = Pets_Has_Clientes(cliente_id=id, pet_id=pet['id'])
                            print(pets_has_clientes)
                            db.session.add(pets_has_clientes)
                            db.session.commit()
                
                
            for x in db_pet_index:
                if x not in lista_pet_index:
                    try:
                        pets_has_clientes = Pets_Has_Clientes.query.filter_by(cliente_id=id, pet_id=x).one()
                        print(pets_has_clientes)
                        db.session.delete(pets_has_clientes)
                    except:
                        db.session.commit()
            db.session.commit()
            
            for x in db_pet_index:
                pets_has_clientes = Pets_Has_Clientes.query.filter_by(pet_id=x).all()
                if len(pets_has_clientes) == 0:
                    try:
                        pet_to_delete = Pet.query.filter_by(id=x).first()
                        db.session.delete(pet_to_delete)
                        db.session.commit()
                    except:
                        db.session.commit()

            return jsonify({'sucesso':'Cliente alterado'})
        else:
            return jsonify({'erro':'Cliente nao encontrado'})
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'erro':'Nao foi possivel acessar os dados'})