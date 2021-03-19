from petshow_api import db

class Tamanho(db.Model):

    __tablename__ = 'tamanho'
    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(15))
    produto = db.relationship('Produto', backref='tamanho', lazy=True)

    def serialize(self):
        return {'id':self.id, 'descricao':self.descricao}