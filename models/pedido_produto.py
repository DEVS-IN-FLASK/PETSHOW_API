from flask_sqlalchemy import SQLAlchemy
from petshow_api import db

pedido_produto = db.Table('pedido_produto',
db.Column('pedido_id', db.Integer, db.ForeignKey('pedido.id'), primary_key=True),
db.Column('produto_id', db.Integer, db.ForeignKey('produto.id'), primary_key=True)
)
