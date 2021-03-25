from petshow_api import db

class Pedido_Produto(db.Model):

    __tablename__="pedido_produto"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    quantidade = db.Column(db.Integer)
    total = db.Column(db.Float)
    preco = db.Column(db.Float)

    def serialize(self):
        return {'id':self.id,'quantidade':self.quantidade,'total':self.total,'preco':self.preco}