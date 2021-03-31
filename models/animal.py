from enum import unique

from sqlalchemy.sql.schema import UniqueConstraint
from petshow_api import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

class Animal(db.Model):

    __tablename__ = 'animais'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    animal = db.Column(db.String(15), nullable=False, unique=True)
    produtos = db.relationship('Produto', backref='animal')
    __table_args__ = (Index('animal_idx', "animal"), )

    def serialize(self):
        return {'id':self.id, 'animal':self.animal}
