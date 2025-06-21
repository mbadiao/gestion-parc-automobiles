from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:motdepasse@localhost:5432/gestion_parc'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'cle_secrete'

    db.init_app(app)
    login_manager.init_app(app)

    # ✅ Bon import selon ta structure
    from app.routes import register_blueprints
    register_blueprints(app)

    return app
