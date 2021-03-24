from petshow_api import db

class Cliente(db.Model):

    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(45))
    email = db.Column(db.String(60))
    cpf = db.Column(db.String(11))

    def serialize(self):
        return {'id':self.id,'nome':self.nome,'email':self.email,'cpf':self.cpf}