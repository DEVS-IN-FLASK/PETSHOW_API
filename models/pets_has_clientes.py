from petshow_api import db

class Pets_Has_Clientes(db.Model):
    __tablename__ = 'pets_has_clientes'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))#, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))#, primary_key=True)
    
    def __repr__(self):
        return f"<Cliente {self.cliente_id} Has Pet {self.pet_id}>"
    
    def serialize(self):
        return {"id": self.id,
                "cliente_id": self.cliente_id,
                "pet_id": self.pet_id,
                }