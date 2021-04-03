from petshow_api import db
from sqlalchemy import ForeignKey

class Pedido_Produto(db.Model):

    __tablename__="pedido_produto"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    quantidade = db.Column(db.Integer)
    total = db.Column(db.Float)
    preco = db.Column(db.Float)
    pedido_id = db.Column(db.Integer,db.ForeignKey('pedidos.id'))
    produto_id = db.Column(db.Integer,db.ForeignKey('produtos.id'))

    def serialize(self):
        return {'id':self.id,'quantidade':self.quantidade,'total':self.total,'preco':self.preco,'pedido_id':self.pedido_id,'produto_id':self.produto_id}