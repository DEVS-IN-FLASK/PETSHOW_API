from petshow_api import db

class Usuario(db.Model):

    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(25),nullable=False)
    senha = db.Column(db.String(20),nullable=False)
    login = db.Column(db.String(15),nullable=False,unique=True)

    def serialize(self):
        return {'id':self.id, 'nome':self.nome,'senha':self.senha,'login':self.login }