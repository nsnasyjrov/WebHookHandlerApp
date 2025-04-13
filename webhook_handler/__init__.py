from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


__all__ = "main"

main_blueprint = Blueprint("main", __name__)

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "over-strong-secret-key"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"