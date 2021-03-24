from petshow_api import db

class Tamanho(db.Model):

    __tablename__ = 'tamanhos'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    tamanho = db.Column(db.String(40))


    
    def serialize(self):
        return {'id':self.id, 'tamanho':self.tamanho}