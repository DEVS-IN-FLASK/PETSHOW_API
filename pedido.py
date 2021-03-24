from petshow_api import db

class Pedido(db.Model):

    __tablename__="pedidos"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    data = db.Column(db.DateTime,nullable=False)
    observacao = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {'id':self.id,'data':self.data,'observacao':self.observacao}