from pet import db

class Marca(db.Model):

    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(40))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))

    
    def serialize(self):
        return {'id':self.id, 'descricao':self.descricao}