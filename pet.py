from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://othtixrbfjlhlq:b9a8949c6208ca7d6203efe5e05049f1bfa71d1ba040ed94a23b28bdd5291679@ec2-54-145-102-149.compute-1.amazonaws.com:5432/d6f5ivqn159sv1'
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
        users = requests.get("https://petshow-api.herokuapp.com/usuarios/").json()
        return render_template('index.html', usuario = users)
     
        prods = requests.get("https://petshow-api.herokuapp.com/produtos/").json()
        return render_template('index.html', produto = prods)
        
    return app  
   