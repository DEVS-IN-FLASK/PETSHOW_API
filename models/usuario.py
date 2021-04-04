from petshow_api import db

class Usuario(db.Model):

    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(25),nullable=False)
    senha = db.Column(db.String(128),nullable=False)
    login = db.Column(db.String(15),nullable=False,unique=True)
    tipo = db.Column(db.String(15),nullable=False)
#    pedidos = db.relationship('Pedido',backref='pedidos')
#    produtos = db.relationship('Produto',backref='produtos')

    def serialize(self):
        return {'id':self.id,'nome':self.nome,'login':self.login,'tipo':self.tipo }