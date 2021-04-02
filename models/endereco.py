from petshow_api import db

class Endereco(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(60), nullable=False)
    numero = db.Column(db.String(10), nullable=False, default="SN")
    cep = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(45), nullable=False)
    cidade = db.Column(db.String(45), nullable=False)
    uf = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f'<Endereco {self.rua}>'

    def serialize(self):
        return {"id": self.id,
                "rua": self.rua,
                "numero": self.numero,
                "bairro": self.bairro,
                "cep": self.cep,
                "cidade": self.cidade,
                "uf": self.uf}