from .auth import auth_bp
from .conducteur import conducteur_bp
from .admin import admin_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(conducteur_bp)
    app.register_blueprint(admin_bp)
