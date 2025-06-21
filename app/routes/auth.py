from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.forms import ConnexionForm
from app.models import Utilisateur
from .. import db, login_manager

auth_bp = Blueprint("auth", __name__)

# Fonction de chargement de l'utilisateur pour Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))

# Page de connexion
@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        if current_user.role == 'admin':
            return redirect(url_for("admin.dashboard"))
        else:
            return redirect(url_for("conducteur.dashboard"))

    form = ConnexionForm()
    if form.validate_on_submit():
        user = Utilisateur.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.mot_de_passe, form.mot_de_passe.data):
            login_user(user, remember=form.se_souvenir.data)
            flash("Connexion réussie ✅", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("conducteur.dashboard" if user.role == "conducteur" else "admin.dashboard"))
        else:
            flash("Email ou mot de passe incorrect ❌", "danger")

    return render_template("login.html", form=form)

# Déconnexion
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Déconnexion réussie.", "info")
    return redirect(url_for("auth.login"))
