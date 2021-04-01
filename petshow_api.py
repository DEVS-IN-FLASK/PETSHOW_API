from flask import Flask, render_template, url_for
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    '''Banco SQlite local'''
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petdb.sqlite'
    '''Banco Postgres local'''
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:819246@localhost:5432/petdb'

    '''Banco Postgres Heroku (ativo)'''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://nuenrexvutummr:e8af86aaf4e99a011914e701532b0fc9bb7b9588b34158cce47e2e921f2ed0c7@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dse9kl9ve57mv'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from usuarios import usuarios_app
    app.register_blueprint(usuarios_app)

    from produtos import produtos_app
    app.register_blueprint(produtos_app)

    from clientes import clientes_app
    app.register_blueprint(clientes_app)

    db.init_app(app)    

    with app.app_context():
        db.create_all()
            
        @app.route("/")
           
        def all():
        
#            users = requests.get("http://127.0.0.1:5000/usuarios/").json()
            users = requests.get("https://petshow-api.herokuapp.com/usuarios/").json()
            return render_template('index.html', usuario = users)
     
            prods = requests.get("https://petshow-api.herokuapp.com/produtos/").json()
            return render_template('index.html', produto = prods)

            cli = requests.get("https://petshow-api.herokuapp.com/clientes").json()
            return render_template('index.html', cliente = cli)

        
        return app