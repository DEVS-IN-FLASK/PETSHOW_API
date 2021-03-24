from petshow_api import db

class Pet(db.Model):

    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(45))
    raca = db.Column(db.String(45))
    porte = db.Column(db.String(10))
    genero = db.Column(db.String(1))
    especie = db.Column(db.String(15))
 
    def serialize(self):
        return {'id':self.id,'nome':self.nome,'raca':self.raca,'porte':self.porte,'genero':self.genero,'especie':self.especie}