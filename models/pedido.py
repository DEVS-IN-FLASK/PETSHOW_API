from petshow_api import db

class Pedido(db.Model):

    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    data = db.Column(db.String)  #Alterar depois para datetime, pois o sqlite não aceita
    observacao = db.Column(db.String(200))
    usuario = db.ForeignKey('Usuario',null=True)
    cliente = db.ForeignKey('Cliente',null=True)
    situacao = db.ForeignKey('Situacao',null=True)
  
    def serialize(self):
        return {'id':self.id, 'data':self.data, 'observacao':self.observacao, 'usuario':self.usuario, 'cliente':self.cliente, 'situacao':self.situacao}