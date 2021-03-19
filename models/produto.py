from petshow_api import db
from sqlalchemy import ForeignKey, Boolean 
from sqlalchemy.orm import relationship, backref 

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
#    marca = db.relationship("Marca")

#    id_tamanho = db.Column(db.ForeignKey('tamanho.id_tamanho'))
#    tamanho = db.relationship('Tamanho', back_populates="produtos")
#    fk_tamanho_id = db.Column(db.Integer, db.ForeignKey('tamanho.id'))


    #id_marca = db.Column(db.ForeignKey('marca.id_marca'))
    #marca = db.relationship('Marca', backref=db.backref('produtos', lazy=True))

    #id_tipo = db.Column(db.ForeignKey('tipo.id_tipo'))
    #tipo = db.relationship('Tipo', backref=db.backref('produtos', lazy=True))

    def serialize(self):
        return {'id':self.id,'descricao':self.descricao,'modelo':self.modelo,'cod_barras':self.cod_barras, 
        'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'foto':self.foto}
    #    'tamanho':self.tamanho,
    #    'marca':self.marca,'tipo':self.tipo}
