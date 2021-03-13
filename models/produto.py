from pet import db

class Produto(db.Model):

    __tablename__="produtos"
    id_produto = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    descricao = db.Column(db.String(255),nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    cod_barras = db.Column(db.Integer,nullable=False)
    porcentagem = db.Column(db.Float,nullable=False)
    preco_custo = db.Column(db.Float,nullable=False)
    preco_venda = db.Column(db.Float,nullable=False)
    foto = db.Column(db.Binary)
#    tamanho_id = db.Column(db.ForeignKey('tamanho.id_tamanho'))
#    marca_id = db.Column(db.ForeignKey('marca.id_marca'))
#    tipo_id = db.Column(db.ForeignKey('tipo.id_tipo'))

    def serialize(self):
        return {'id_produto':self.id_produto, 'descricao':self.descricao,'modelo':self.modelo, 'cod_barras':self.cod_barras, 
        'porcentagem':self.porcentagem,'preco_custo':self.preco_custo,'preco_venda':self.preco_venda,'foto':self.foto}
#        'tamanho_id':self.tamanho_id,'marca_id':self.marca_id, 'tipo_id':self.tipo_id }