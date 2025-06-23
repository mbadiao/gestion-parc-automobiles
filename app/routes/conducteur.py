from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Utilisateur, ConducteurProfil, VehiculeAssignation, Vehicule, Itineraire
from app.forms import ItineraireForm
from datetime import date

conducteur_bp = Blueprint("conducteur", __name__, url_prefix="/conducteur")

@conducteur_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role != 'conducteur':
        return redirect(url_for('auth.login'))

    profil = ConducteurProfil.query.filter_by(utilisateur_id=current_user.id).first()
    assignation = VehiculeAssignation.query.filter_by(conducteur_id=current_user.id, active=True).first()
    vehicule = Vehicule.query.get(assignation.vehicule_id) if assignation else None
    trajets_query = Itineraire.query.filter_by(conducteur_id=current_user.id).order_by(Itineraire.date_trajet.desc()).limit(10).all()

    # Convertir les objets Itineraire en dictionnaires pour la sérialisation JSON
    trajets = []
    for trajet in trajets_query:
        trajets.append({
            'id': trajet.id,
            'date_trajet': trajet.date_trajet.strftime('%Y-%m-%d') if trajet.date_trajet else '',
            'lieu_depart': trajet.lieu_depart,
            'lieu_arrivee': trajet.lieu_arrivee,
            'distance_km': float(trajet.distance_km) if trajet.distance_km else 0,
            'duree_minutes': trajet.duree_minutes,
            'polyline': trajet.polyline
        })

    return render_template("conducteur/dashboard.html", profil=profil, vehicule=vehicule, trajets=trajets)

@conducteur_bp.route("/itineraire", methods=["GET", "POST"])
@login_required
def nouvel_itineraire():
    if current_user.role != 'conducteur':
        return redirect(url_for('auth.login'))

    form = ItineraireForm()
    assignation = VehiculeAssignation.query.filter_by(conducteur_id=current_user.id, active=True).first()
    vehicule = Vehicule.query.get(assignation.vehicule_id) if assignation else None

    if not vehicule:
        flash("Aucun véhicule ne vous a été attribué.", "warning")
        return redirect(url_for("conducteur.dashboard"))

    if form.validate_on_submit():
        trajet = Itineraire(
            conducteur_id=current_user.id,
            vehicule_id=vehicule.id,
            date_trajet=form.date_trajet.data,
            lieu_depart=form.lieu_depart.data,
            lieu_arrivee=form.lieu_arrivee.data,
            distance_km=form.distance_km.data,
            duree_minutes=form.duree_minutes.data,
            polyline=form.polyline.data  # Optionnel, sera rempli via JS avec Leaflet
        )
        db.session.add(trajet)
        db.session.commit()
        flash("Itinéraire ajouté avec succès ✅", "success")
        return redirect(url_for("conducteur.dashboard"))

    return render_template("conducteur/itineraire_form.html", form=form, vehicule=vehicule)
