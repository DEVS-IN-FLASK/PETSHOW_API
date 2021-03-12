from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://hkcgbbjbyigqbf:8f5b9914ac293e1a2dab2666eacf3919bb52274d6223b4734967b947aaf9f0a4@ec2-18-214-208-89.compute-1.amazonaws.com:5432/d5deu3o52r4cu9'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from usuarios import usuarios_app
    app.register_blueprint(usuarios_app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    @app.route("/")
    def all():
        users = requests.get("http://localhost:5000/usuarios/").json()
        return render_template('index.html', usuario = users)
     
    return app  
    #linha test git