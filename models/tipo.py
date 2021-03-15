from pet import db

class Tipo(db.Model):

    __tablename__ = 'tipo'
    id_tipo = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(15))

    def serialize(self):
        return {'id_tipo':self.id_tipo, 'descricao':self.descricao}
