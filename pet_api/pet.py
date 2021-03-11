from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://fmgzzsnk:bmOfF6Vypzx9tAdRNiXUtvg4sJVA0-aO@ziggy.db.elephantsql.com:5432/fmgzzsnk'
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