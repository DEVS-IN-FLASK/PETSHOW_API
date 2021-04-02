from petshow_api import db

class Telefone(db.Model):
    __tablename__ = 'telefones'
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(11), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

    def __repr__(self):
        return f'<Telefone {self.telefone}>'

    def serialize(self):
        return {"id": self.id,
                "cliente_id": self.cliente_id,
                "telefone": self.telefone}