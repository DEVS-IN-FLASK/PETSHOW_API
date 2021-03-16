from pet import db

class Produto(db.Model):

    __tablename__="produtos"
    id_produto = db.Column(db.Integer, primary_key=True,nullable=True,autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer,nullable=False, unique=True)
    porcentagem = db.Column(db.Float)
    preco_custo = db.Column(db.Float)
    preco_venda = db.Column(db.Float)
    foto = db.Column(db.Binary)
    id_tamanho = db.Column(db.ForeignKey('tamanho.id_tamanho'),nullable=False)
    tamanho = db.relationship('Tamanho', backref=db.backref('produtos', lazy=True))
    id_marca = db.Column(db.ForeignKey('marca.id_marca'))
    marca = db.relationship('Marca', backref=db.backref('produtos', lazy=True))
    id_tipo = db.Column(db.ForeignKey('tipo.id_tipo'))
    tipo = db.relationship('Tipo', backref=db.backref('produtos', lazy=True))

    def serialize(self):
        return {'id_produto':self.id_produto,'descricao':self.descricao,'modelo':self.modelo,'cod_barras':self.cod_barras, 
        'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'foto':self.foto,
        'tamanho':self.tamanho,'marca':self.marca,'tipo':self.tipo}
