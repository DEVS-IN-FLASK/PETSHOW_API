from petshow_api import db
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

class Pedido(db.Model):

    __tablename__="pedidos"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    data = db.Column(db.DateTime,nullable=False)
    observacao = db.Column(db.String(200))
    situacao_id = db.Column(db.Integer,db.ForeignKey('situacao.id'))
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuarios.id'))
    cliente_id = db.Column(db.Integer,db.ForeignKey('clientes.id'))

    def serialize(self):
        return {'id':self.id,'data':self.data,'observacao':self.observacao,'situacao_id':self.situacao_id, 'usuario_id':self.usuario_id,'cliente_id':self.cliente_id}