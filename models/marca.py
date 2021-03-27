from models import produto
from petshow_api import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

class Marca(db.Model):

    __tablename__ = 'marcas'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    marca = db.Column(db.String(40))
    produtos = db.relationship('Produto',backref='marca')
    __table_args__ = (Index('marca_idx', "marca"), )

    def serialize(self):
        return {'id':self.id, 'marca':self.marca}