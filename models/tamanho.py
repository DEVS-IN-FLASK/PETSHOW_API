from pet import db

class Tamanho(db.Model):

    __tablename__ = 'tamanho'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(15))
#    fk_produto_id=db.Column(db.Integer, db.ForeignKey('produto.id'))
 #   fk_produto_id = db.relationship("produto.id")
#    produtos = db.relationship("Produto", uselist=False, back_populates="tamanho")

    def serialize(self):
        return {'id':self.id, 'descricao':self.descricao}