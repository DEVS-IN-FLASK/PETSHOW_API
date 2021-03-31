from petshow_api import db
from sqlalchemy import ForeignKey, Boolean 
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

class Produto(db.Model):    

    __tablename__="produtos"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer,unique=True, nullable=False)
    porcentagem = db.Column(db.Float)
    preco_custo = db.Column(db.Float)   
    preco_venda = db.Column(db.Float)
    foto = db.Column(db.Binary)
    quantidade = db.Column(db.Integer)
    marca_id = db.Column(db.Integer,db.ForeignKey('marcas.id'))
    animal_id = db.Column(db.Integer,db.ForeignKey('animais.id'))
    tamanho_id = db.Column(db.Integer,db.ForeignKey('tamanhos.id'))

    def serialize(self):
        return {'id':self.id,'descricao':self.descricao,'modelo':self.modelo,'cod_barras':self.cod_barras, 
        'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'foto':self.foto,'quantidade':self.quantidade,'marca_id':self.marca_id,'animal_id':self.animal_id,'tamanho_id':self.tamanho_id}

