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
    app.config.from_pyfile('config.py')

    jwt = JWTManager(app)
    

    url = 'https://petshow-api.herokuapp.com/'

    from blueprints.usuarios import usuarios_app
    app.register_blueprint(usuarios_app)

    from blueprints.produtos import produtos_app
    app.register_blueprint(produtos_app)

    from blueprints.clientes import clientes_app
    app.register_blueprint(clientes_app)
    
    from blueprints.pedidos import pedidos_app
    app.register_blueprint(pedidos_app)
    
    from blueprints.testes import testes_app
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