from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Vehicule, Utilisateur, Itineraire
from app.forms import VehiculeForm
from datetime import datetime

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@login_required
def dashboard_admin():
    if current_user.role != 'admin':
        flash("Accès réservé à l'administrateur.", "danger")
        return redirect(url_for('auth.login'))

    filtre_statut = request.args.get('filtre_statut')
    date_filtre = request.args.get('date')
    conducteur_filtre = request.args.get('conducteur_id')

    # Filtrage véhicules
    vehicules = Vehicule.query
    if filtre_statut == "disponible":
        vehicules = vehicules.filter_by(disponible=True)
    elif filtre_statut == "attribue":
        vehicules = vehicules.filter_by(disponible=False)
    vehicules = vehicules.all()

    # Tous les conducteurs
    conducteurs = Utilisateur.query.filter_by(role='conducteur').all()

    # Filtrage des itinéraires
    itineraires = Itineraire.query

    if date_filtre:
        try:
            date_obj = datetime.strptime(date_filtre, "%Y-%m-%d")
            itineraires = itineraires.filter_by(date_trajet=date_obj.date())
        except ValueError:
            flash("Format de date invalide", "warning")

    if conducteur_filtre:
        itineraires = itineraires.filter_by(conducteur_id=int(conducteur_filtre))

    itineraire_data = [
        {
            "polyline": i.polyline,
            "conducteur_id": i.conducteur_id,
            "date_trajet": i.date_trajet.strftime("%Y-%m-%d")
        }
        for i in itineraires
    ]

    return render_template("admin/dashboard.html",
                           vehicules=vehicules,
                           conducteurs=conducteurs,
                           filtre_statut=filtre_statut,
                           date_filtre=date_filtre,
                           conducteur_filtre=conducteur_filtre,
                           itineraire_data=itineraire_data)


@admin_bp.route("/vehicule/ajouter", methods=["GET", "POST"])
@login_required
def ajouter_vehicule():
    if current_user.role != 'admin':
        flash("Accès interdit", "danger")
        return redirect(url_for("auth.login"))

    form = VehiculeForm()

    if form.validate_on_submit():
        vehicule = Vehicule(
            marque=form.marque.data,
            modele=form.modele.data,
            annee=form.annee.data,
            immatriculation=form.immatriculation.data,
            couleur_exterieure=form.couleur_exterieure.data,
            couleur_interieure=form.couleur_interieure.data,
            type_carburant=form.type_carburant.data,
            transmission=form.transmission.data,
            puissance=form.puissance.data,
            kilometrage=form.kilometrage.data,
            disponible=True
        )
        db.session.add(vehicule)
        db.session.commit()
        flash("Véhicule ajouté avec succès", "success")
        return redirect(url_for("admin.dashboard_admin"))

    return render_template("admin/ajouter_vehicule.html", form=form)


@admin_bp.route("/vehicule/modifier/<int:vehicule_id>", methods=["GET", "POST"])
@login_required
def modifier_vehicule(vehicule_id):
    if current_user.role != 'admin':
        flash("Accès interdit", "danger")
        return redirect(url_for("auth.login"))

    vehicule = Vehicule.query.get_or_404(vehicule_id)
    form = VehiculeForm(obj=vehicule)

    if form.validate_on_submit():
        form.populate_obj(vehicule)
        db.session.commit()
        flash("Véhicule mis à jour", "success")
        return redirect(url_for("admin.dashboard_admin"))

    return render_template("admin/modifier_vehicule.html", form=form)


@admin_bp.route("/vehicule/attribuer/<int:conducteur_id>", methods=["GET", "POST"])
@login_required
def attribuer_vehicule(conducteur_id):
    if current_user.role != 'admin':
        flash("Accès interdit", "danger")
        return redirect(url_for("auth.login"))

    conducteur = Utilisateur.query.get_or_404(conducteur_id)
    vehicules_dispos = Vehicule.query.filter_by(disponible=True).all()

    if request.method == "POST":
        vehicule_id = int(request.form["vehicule_id"])
        vehicule = Vehicule.query.get(vehicule_id)
        if vehicule:
            # Marquer véhicule comme attribué
            vehicule.disponible = False
            db.session.commit()

            # Ajouter une assignation (bonus)
            # ...

            flash("Véhicule attribué avec succès", "success")
            return redirect(url_for("admin.dashboard_admin"))

    return render_template("admin/attribuer_vehicule.html",
                           conducteur=conducteur,
                           vehicules=vehicules_dispos)
