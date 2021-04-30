from petshow_api import db
from sqlalchemy import ForeignKey

class Pedido_Produto(db.Model):

    __tablename__="pedido_produto"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    total = db.Column(db.Float)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer, default=0)
    pedido_id = db.Column(db.Integer,db.ForeignKey('pedidos.id'),nullable=True)
    pedido = db.relationship("Pedido")
    produto_id = db.Column(db.Integer,db.ForeignKey('produtos.id'),nullable=True)
    produto = db.relationship("Produto")

    def serialize(self):
        return {'id':self.id,'quantidade':self.quantidade,'total':self.total,'preco':self.preco,'pedido':self.pedido,'produto':self.produto}