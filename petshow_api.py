from flask import Flask, render_template, url_for
#from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS, cross_origin
import requests


from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
#from usuarios import authenticate, identity

#migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'devsinflaskpetshowapi'
    jwt = JWTManager(app)
    
#    CORS(app, support_credentials=True)

    '''Banco SQlite local'''
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petdb.sqlite'
    '''Banco Postgres local'''
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:819246@localhost:5432/petdb'

    '''Banco Postgres Heroku (ativo)'''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://nuenrexvutummr:e8af86aaf4e99a011914e701532b0fc9bb7b9588b34158cce47e2e921f2ed0c7@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dse9kl9ve57mv'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    '''URL localhost'''
#    url = 'http://127.0.0.1:5000/'
    '''URL Heroku'''
    url = 'https://petshow-api.herokuapp.com/'

    from usuarios import usuarios_app
    app.register_blueprint(usuarios_app)

    from produtos import produtos_app
    app.register_blueprint(produtos_app)

    from clientes import clientes_app
    app.register_blueprint(clientes_app)
    
    from pedidos import pedidos_app
    app.register_blueprint(pedidos_app)
    
    from testes import testes_app
    app.register_blueprint(testes_app)
    

    db.init_app(app)
    
 

    with app.app_context():
        db.create_all()
            
        @app.route("/")

           
        def all():
        
#            users = requests.get("http://127.0.0.1:5000/usuarios/").json()
            users = requests.get(f"{url}usuarios/").json()
            return render_template('index.html', usuario = users)
     
            prods = requests.get(f"{url}produtos/").json()
            return render_template('index.html', produto = prods)

            cli = requests.get(f"{url}clientes").json()
            return render_template('index.html', cliente = cli)
        
            ped = requests.get(f"{url}pedidos").json()
            return render_template('index.html', cliente = ped)

        
        return app