from enum import unique
from petshow_api import db
from sqlalchemy import ForeignKey, Boolean 
from sqlalchemy.orm import relationship

class Cliente(db.Model):

    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(45))
    email = db.Column(db.String(60))
    cpf = db.Column(db.String(11),unique=True)
    endereco_id = db.Column(db.Integer,db.ForeignKey('enderecos.id'))

    def serialize(self):
        return {'id':self.id,'nome':self.nome,'email':self.email,'cpf':self.cpf,'endereco_id':self.endereco_id}