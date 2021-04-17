from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Cliente, Telefone, Endereco, Pet, Pets_Has_Clientes
from petshow_api import db

clientes_app = Blueprint('clientes', __name__,url_prefix='/clientes')

# inclusão e consulta de clientes e pets
@clientes_app.route('/',methods=['GET', 'POST'])
def clientes():
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

# remocao de cliente, telefone, endereco e relacionamento com pet
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

@clientes_app.route('/<id>/alterar/', methods=['PUT'])
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

            #db.session.commit()
            
            lista_tel = dados['telefones']
            busca_tel = Telefone.query.filter_by(cliente_id=cliente.id).all()
            for tel in busca_tel:
                db.session.delete(tel)
            for tel in lista_tel:
                numero = Telefone(telefone=tel['telefone'], cliente_id=cliente.id)
                db.session.add(numero)

            db.session.commit()

            return jsonify({'sucesso':'Cliente alterado'})
        else:
            return jsonify({'erro':'Cliente nao encontrado'})
    except Exception:
        db.session.rollback()
        return jsonify({'erro':'Nao foi possivel acessar os dados'})