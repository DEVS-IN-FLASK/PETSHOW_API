from petshow_api import db

class Cliente(db.Model):

    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = db.Column(db.String(45))
    email = db.Column(db.String(60))
    cpf = db.Column(db.Bigint(11))
    endereco_id = db.ForeignKey('endereco_id',null=True)
  
    def serialize(self):
        return {'id':self.id, 'nome':self.nome, 'email':self.email, 'cpf':self.cpf, 'endereco_id':self.endereco_id}