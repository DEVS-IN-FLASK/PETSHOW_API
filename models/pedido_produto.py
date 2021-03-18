from pet import db

class Pedido_Produto(db.Model):

    __tablename__ = 'pedido_produto'

    pedido_id = db.ForeignKey('Pedido',null=True)
    produto_id = db.ForeignKey('Produto',null=True)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)
    total = db.Column(db.Float)
  
    def serialize(self):
        return {'pedido_id':self.pedido_id,'produto_id':self.produto_id,'quantidade':self.quantidade,'preco':self.preco,'total':self.total}