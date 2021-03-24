from petshow_api import db

class Marca(db.Model):

    __tablename__ = 'marcas'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    marca = db.Column(db.String(40))

  
    def serialize(self):
        return {'id':self.id, 'marca':self.marca}