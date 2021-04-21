from petshow_api import db
from sqlalchemy import ForeignKey

class Pedido(db.Model):

    __tablename__="pedidos"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    data = db.Column(db.DateTime, server_default=UtcNow())
    observacao = db.Column(db.String(200), nullable=False)
#    quantidade = db.Column(db.Integer)
    situacao_id = db.Column(db.Integer,db.ForeignKey('situacao.id'))    
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuarios.id'))
    cliente_id = db.Column(db.Integer,db.ForeignKey('clientes.id'))

#    pedido_produto = db.relationship('Pedido', secondary=pedido_produto, lazy='subquery',
#        backref=db.backref('produtos', lazy=True))

    def serialize(self):
        return {'id':self.id,'data':self.data,'observacao':self.observacao,'situacao_id':self.situacao_id, 'usuario_id':self.usuario_id,'cliente_id':self.cliente_id}