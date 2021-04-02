from petshow_api import db
from sqlalchemy import Index


class Endereco(db.Model):

    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    rua = db.Column(db.String(60))
    cep = db.Column(db.String(8))
    bairro = db.Column(db.String(45))
    cidade = db.Column(db.String(45))
    uf = db.Column(db.String(2))
    clientes = db.relationship('Cliente',backref='endereco')

    def serialize(self):
        return {'id':self.id,'rua':self.rua,'cep':self.cep,'bairro':self.bairro,'cidade':self.cidade,'uf':self.uf}