from petshow_api import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

class Tamanho(db.Model):

    __tablename__ = 'tamanhos'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    tamanho = db.Column(db.String(40), nullable=False)
    produtos = db.relationship('Produto',backref='tamanho')
    __table_args__ = (Index('tamanho_idx', "tamanho"), )
 
    def serialize(self):
        return {'id':self.id, 'descricao':self.descricao}