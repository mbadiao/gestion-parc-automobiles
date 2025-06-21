from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv() 
login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = (f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # ✅ Bon import selon ta structure
    from app.routes import register_blueprints
    register_blueprints(app)

    return app
