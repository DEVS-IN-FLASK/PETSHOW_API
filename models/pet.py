from petshow_api import db

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    raca = db.Column(db.String(45), nullable=False, default="SRD")
    porte = db.Column(db.String(10), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    especie = db.Column(db.String(15), nullable=False)

    clientes = db.relationship('Cliente', secondary='pets_has_clientes')

    def __repr__(self):
        return f"<Pet {self.nome}>"

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "raca": self.raca,
                "porte": self.porte,
                "genero": self.genero,
                "especie": self.especie}