from petshow_api import db

class Telefone(db.Model):

    __tablename__ = 'telefones'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    telefone = db.Column(db.String(11))

    def serialize(self):
        return {'id':self.id, 'telefone':self.telefone}