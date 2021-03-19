from petshow_api import db
from .pedido import Pedido
from .produto import Produto

class Pedido_Produto(db.Model):

    __tablename__ = 'pedido_produto'

    # id adicionado apenas para o programa rodar, ão existe pois é uma tabela de relacionamento, situação a analisar
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)

    pedido_id = db.Column(db.Integer, db.ForeignKey(Pedido.id), nullable = False)
    pedido = db.relationship("Pessoa")

    produto_id = db.Column(db.Integer, db.ForeignKey(Produto.id), nullable = False)
    produto_id = db.relationship("Produto")
#    pedido_id = db.ForeignKey('Pedido',null=True)
#    produto_id = db.ForeignKey('Produto',null=True)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)
    total = db.Column(db.Float)
  
    def serialize(self):
        return {'pedido_id':self.pedido_id,'produto_id':self.produto_id,'quantidade':self.quantidade,'preco':self.preco,'total':self.total}