from petshow_api import db

class Produto(db.Model):

    __tablename__="produto"
    id = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer,nullable=False, unique=True)
    porcentagem = db.Column(db.Float)
    preco_custo = db.Column(db.Float)
    preco_venda = db.Column(db.Float)
    foto = db.Column(db.Binary)
    marca = db.relationship('Marca')
    animal = db.relationship('Animal')
    tamanho = db.relationship('Tamanho')

   
    def serialize(self):
        return {'id':self.id,'descricao':self.descricao,'modelo':self.modelo,'cod_barras':self.cod_barras,'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'foto':self.foto,'marca':self.marca,'animal':self.animal,'tamanho':self.tamanho}