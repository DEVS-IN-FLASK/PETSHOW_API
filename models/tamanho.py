from pet import db

class Tamanho(db.Model):

    __tablename__ = 'tamanho'
    id_tamanho = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(15))
#    produtos = db.relationship("Produto", uselist=False, back_populates="tamanho")

    def serialize(self):
        return {'id_tamanho':self.id_tamanho, 'descricao':self.descricao}