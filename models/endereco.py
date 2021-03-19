from petshow_api import db

class Endereco(db.Model):

    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    rua = db.Column(db.String(15))
    cep = db.Column(db.String(8))
    bairro = db.Column(db.String(45))
    cidade = db.Column(db.String(45))
    uf = db.Column(db.String(2))

    def serialize(self):
        return {'id':self.id, 'rua':self.rua, 'cep':self.cep, 'bairro':self.bairro, 'cidade':self.cidade, 'uf':self.uf}