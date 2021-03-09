from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////temp/petbd.db"

    return app