from pet import db

class Produto(db.Model):

    __tablename__="produtos"
    id_produto = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer(13),nullable=False)
    porcentagem = db.Column(db.Decimal,nullable=False)
    tamanho_id = db.Coumn(ForeignKey )




    def serialize(self):
        return {'id':self.id, 'nome':self.nome,'senha':self.senha,'login':self.login }