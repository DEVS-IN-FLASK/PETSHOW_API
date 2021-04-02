from petshow_api import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    endereco = db.relationship('Endereco')
    endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'))
    telefone = db.relationship('Telefone')
    #telefone_id = db.Column(db.Integer, db.ForeignKey('telefones.id'))
    pets = db.relationship('Pet', secondary='pets_has_clientes')
   
    def __repr__(self):
        return f"<Cliente {self.nome}, Endereço {self.endereco}>"

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "cpf": self.cpf,
                "email": self.email,
                "endereco": self.endereco.serialize(),
                }

