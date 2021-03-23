from petshow_api import db

class Marca(db.Model):

    __tablename__ = 'marcas'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    marca = db.Column(db.String(40))
    produto = db.relationship('Produto', backref='marcas', lazy=True)

#    produtos = db.relationship("Produto", backref ="marcas")

  
    def serialize(self):
        return {'id':self.id, 'marca':self.marca}