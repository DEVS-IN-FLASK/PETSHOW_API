from petshow_api import db
from flask import url_for

class Cliente(db.Model):

    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(45))
    email = db.Column(db.String(60))
    cpf = db.Column(db.String(11))
    endereco = db.relationship('Endereco')
    endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'), nullable=False)
  
    def serialize(self):
        return {'id':self.id, 'nome':self.nome, 'email':self.email, 'cpf':self.cpf, 'endereco':self.endereco.serialize()}