from petshow_api import db
from sqlalchemy import Index
from sqlalchemy.orm import relationship

class Usuario(db.Model):

    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(25),nullable=False)
    senha = db.Column(db.String(128),nullable=False)
    login = db.Column(db.String(15),nullable=False,unique=True)
    tipo = db.Column(db.String(15),nullable=False)
    produtos = db.relationship('Produto',backref='login')
    __table_args__ = (Index('login_idx', "login"), )
    pedidos = db.relationship('Pedido',backref='login')
#    produtos = db.relationship('Produto',backref='produtos')


    def serialize(self):
        return {'id':self.id,'nome':self.nome,'login':self.login,'tipo':self.tipo }