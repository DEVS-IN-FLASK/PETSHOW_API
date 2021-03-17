from pet import db

class Animal(db.Model):

    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    tipo = db.Column(db.String(15))

    def serialize(self):
        return {'id':self.id, 'tipo':self.tipo}
