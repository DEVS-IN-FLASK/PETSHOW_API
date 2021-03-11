from pet import db

class Usuario(db.Model):

    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(15),nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    login = db.Column(db.String(15),nullable=False)

    def serialize(self):
        return {'id':self.id, 'login':self.login, 'nome':self.nome}