from petshow_api import db

class Animal(db.Model):

    __tablename__ = 'animais'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    animal = db.Column(db.String(15))
#    produto = db.relationship('Produto', backref='animal', lazy=True)

    def serialize(self):
        return {'id':self.id, 'animal':self.animal}
