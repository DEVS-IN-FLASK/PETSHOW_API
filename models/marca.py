from petshow_api import db

class Marca(db.Model):

    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(40))
    produto = db.relationship('Produto', backref='marca', lazy=True)

  
    def serialize(self):
        return {'id':self.id, 'descricao':self.descricao}