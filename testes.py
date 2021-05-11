from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Cliente, Telefone, Endereco, Pet, Pets_Has_Clientes, Animal, Pedido, Usuario, Marca, Produto, Tamanho, Situacao, Pedido_Produto
from petshow_api import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

testes_app = Blueprint('testes', __name__,url_prefix='/testes')

@testes_app.route('/')
def preenche_campos():
    usuarios = Usuario.query.all()
    if len(usuarios) == 0:
        dados = [
            ['Admin', 'admin', 'senha', 'gerente'],
            ['Jose', 'jose', 'senha', 'funcionario'],
            ['Maria', 'maria', 'senha', 'gerente']
        ]
        for x in dados:
            usuario = Usuario(nome=x[0], login=x[1], senha=generate_password_hash(x[2]), tipo=x[3])
            db.session.add(usuario)
        db.session.commit()

        db.session.add(Animal(animal='cachorro'))
        db.session.add(Animal(animal='gato'))
        db.session.commit()
        
        dados = [
            ['Floquinho', 'Vira-Lata', 'pequeno', 'm', 1],
            ['Soft Kitty', 'Siamês', 'medio', 'm', 2],
            ['Snoopy', 'Cão branco', 'grande', 'm', 1],
            ['Garfilda', 'Zebrado', 'grande', 'f', 2],
        ]
        
        for x in dados:
            pet = Pet(nome=x[0], raca=x[1], porte=x[2], genero=x[3], animal_id=x[4])
            db.session.add(pet)
        db.session.commit()
        
        dados = [
            ['Rua 01', '23', '060000-160', 'Vila Frente', 'Osasco', 'SP'],
            ['Rua 02', '43', '060020-161', 'Vila Ré', 'Barueri', 'SP'],
            ['Rua 03', '63', '060001-162', 'Vila Vazia', 'Mauá', 'SP']
        ]
        
        for x in dados:
            endereco = Endereco(rua=x[0], numero=x[1], cep=x[2], bairro=x[3], cidade=x[4], uf=x[5])
            db.session.add(endereco)
        db.session.commit()

        dados = [
            ['Beatrix Kiddo', 'beakiddo@kiddo.com', '10000000001', 1, ['01199938884', '01199882244'], [1, 2]],
            ['Bill', 'bill@kill.com', '10000000009', 2, ['01199238884', '01199882244'], [1]],
            ['Rory', 'lorelai@kill.com', '10000000011', 3, ['01199966884', '01199886644'], [4]],
        ]
        
        for x in dados:
            cliente = Cliente(nome=x[0], email=x[1], cpf=x[2], endereco_id=x[3])
            db.session.add(cliente)
            db.session.commit()
            cliente_id = cliente.id
            
            for t in x[4]:
                telefone = Telefone(telefone=t, cliente_id=cliente_id)
                db.session.add(telefone)
            db.session.commit()
            
            for p in x[5]:
                pets_has_clientes = Pets_Has_Clientes(cliente_id=cliente_id, pet_id=p)
                db.session.add(pets_has_clientes)
            db.session.commit()
            
        dados = ['PetDog', 'PetCat']
        
        for m in dados:
            marca = Marca(marca=m)
            db.session.add(marca)
        db.session.commit()
        
        dados = ['P', 'M', 'G']
        for t in dados:
            tamanho = Tamanho(tamanho=t)
            db.session.add(tamanho)
        db.session.commit()
        
        dados = [
            ['Blusa Cão', 'Azul', 'Pullover', '39232839', 10, 100, 120, '', 10, 1, 1, 1, 1],
            ['Blusa Cão', 'Azul', 'Pullover', '39232831', 10, 100, 120, '', 10, 1, 1, 2, 1],
            ['Blusa Cão', 'Azul', 'Pullover', '39232834', 10, 100, 120, '', 10, 1, 1, 3, 1],
            ['Blusa Gato', 'Vermelha', 'Pullover', '39232849', 10, 100, 120, '', 30, 2, 2, 2, 2]
        ]
        
        for p in dados:
            produto = Produto(nome=p[0], descricao=p[1], modelo=p[2], cod_barras=p[3], porcentagem=p[4],
                                preco_custo=p[5], preco_venda=p[6], foto=p[7], quantidade=p[8],
                                marca_id=p[9], animal_id=p[10], tamanho_id=p[11], usuario_id=p[12])
            db.session.add(produto)
        db.session.commit()
        
        dados = ['recebido', 'concluido', 'cancelado']
        
        for s in dados:
            situacao = Situacao(descricao=s)
            db.session.add(situacao)
        db.session.commit()
        
        dados = [
            [datetime.utcnow(), 'separado', 1, 2, 1],
            [datetime.utcnow(), '', 2, 2, 1],
            [datetime.utcnow(), 'cheque sem fundos', 3, 3, 2]
        ]
        
        for p in dados:
            pedido = Pedido(data=p[0], observacao=p[1], situacao_id=p[2], usuario_id=p[3], cliente_id=p[4])
            db.session.add(pedido)
        db.session.commit()
        
        dados = [
            [
                [1, 1, 1, Produto.query.filter_by(id=1).first().preco_venda, Produto.query.filter_by(id=1).first().preco_venda * 1],
                [1, 2, 1, Produto.query.filter_by(id=2).first().preco_venda, Produto.query.filter_by(id=2).first().preco_venda * 1]
            ],
            [
                [2, 1, 2, Produto.query.filter_by(id=1).first().preco_venda, Produto.query.filter_by(id=1).first().preco_venda * 2],
                [2, 2, 1, Produto.query.filter_by(id=2).first().preco_venda, Produto.query.filter_by(id=2).first().preco_venda * 1]
            ],
            [
                [3, 4, 1, Produto.query.filter_by(id=4).first().preco_venda, Produto.query.filter_by(id=4).first().preco_venda * 1]
            ]
        ]
        
        for i in dados:
            for item in i:
                item_pedido = Pedido_Produto(pedido_id=item[0], produto_id=item[1], quantidade=item[2], preco=item[3], total=item[4])
                db.session.add(item_pedido)
            db.session.commit()
            
    return "ok"