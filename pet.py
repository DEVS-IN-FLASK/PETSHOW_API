from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://edtjxfihkbbwcg:aafccf72712d5807c4db728c68af8339b0d09bab37c0f090bf95fb6b11e4a4a2@ec2-52-7-115-250.compute-1.amazonaws.com:5432/d7vlr1mc5qqm2r'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from usuarios import usuarios_app
    app.register_blueprint(usuarios_app)

    from produtos import produtos_app
    app.register_blueprint(produtos_app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    @app.route("/")
    def all():
        users = requests.get("http://localhost:5000/usuarios/").json()
        return render_template('index.html', usuario = users)
     
        prods = requests.get("http://localhost:5000/produtos/").json()
        return render_template('index.html', produto = prods)
        
    return app  
   