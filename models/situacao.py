from petshow_api import db

class Situacao(db.Model):

    __tablename__="situacao"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    descricao = db.Column(db.String(15), nullable=False)
    pedidos = db.relationship('Pedido',backref='situacao')

    def serialize(self):
        return {'id':self.id,'descricao':self.descricao}