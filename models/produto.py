from petshow_api import db
from sqlalchemy import ForeignKey
#from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


class Produto(db.Model):    

    __tablename__="produtos"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    nome = db.Column(db.String(45),nullable=False)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer,unique=True, nullable=False)
    porcentagem = db.Column(db.Float, default=0)
    preco_custo = db.Column(db.Float, default=0)
    preco_venda = db.Column(db.Float, default=0)
    quantidade = db.Column(db.Integer,default=0)
    foto = db.Column(db.String(255), nullable=True)
    marca_id = db.Column(db.Integer,db.ForeignKey('marcas.id'))
    animal_id = db.Column(db.Integer,db.ForeignKey('animais.id'))
    tamanho_id = db.Column(db.Integer,db.ForeignKey('tamanhos.id'))
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuarios.id'),nullable=True)

#    pedido_produto = db.relationship('Pedido', secondary=pedido_produto, lazy='subquery',
#        backref=db.backref('produtos', lazy=True))


    def serialize(self):
        return {'id':self.id,'nome':self.nome,'descricao':self.descricao,'modelo':self.modelo,'cod_barras':self.cod_barras, 
        'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'quantidade':self.quantidade,'foto':self.foto,
        'marca_id':self.marca_id,'animal_id':self.animal_id,'tamanho_id':self.tamanho_id
        ,'usuario_id':self.usuario_id}

