from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Vehicule, Utilisateur, Itineraire, ConducteurProfil
from sqlalchemy.exc import IntegrityError
from app.forms import VehiculeForm, ConducteurForm
from datetime import datetime, date
from app.models import VehiculeAssignation

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@login_required
def dashboard():
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

    # Conducteurs sans véhicule attribué (basé sur la table d'assignation)
    # On sélectionne les conducteurs qui n'ont pas d'assignation active
    subquery = db.session.query(VehiculeAssignation.conducteur_id).filter(VehiculeAssignation.active == True)
    conducteurs = Utilisateur.query.filter_by(role='conducteur').filter(~Utilisateur.id.in_(subquery)).all()

    # Filtrage des itinéraires
    itineraires = Itineraire.query

    if date_filtre:
        try:
            date_obj = datetime.strptime(date_filtre, "%Y-%m-%d")
            itineraires = itineraires.filter_by(date_trajet=date_obj.date())
        except ValueError:
            flash("Format de date invalide", "warning")



    return render_template("admin/dashboard.html",
                           vehicules=vehicules,
                           conducteurs=conducteurs,
                           filtre_statut=filtre_statut,
                           date_filtre=date_filtre,
                           conducteur_filtre=conducteur_filtre
                          )


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
        try:
            db.session.commit()
            flash("Véhicule ajouté avec succès", "success")
            return redirect(url_for("admin.dashboard"))
        except IntegrityError as e:
            db.session.rollback()
            if "vehicule_immatriculation_key" in str(e.orig):
                flash("Cette immatriculation existe déjà.", "danger")
            else:
                flash("Erreur lors de l'ajout du véhicule.", "danger")
    elif request.method == "POST":
        # Afficher les erreurs du formulaire
        print("Form errors:", form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Erreur dans le champ '{getattr(form, field).label.text}': {error}", "danger")

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
            # Créer une assignation
            assignation = VehiculeAssignation(
                conducteur_id=conducteur.id,
                vehicule_id=vehicule.id,
                date_debut=date.today(),
                active=True
            )
            db.session.add(assignation)
            db.session.commit()
            flash("Véhicule attribué avec succès", "success")
            return redirect(url_for("admin.dashboard"))

    return render_template("admin/attribuer_vehicule.html",
                           conducteur=conducteur,
                           vehicules=vehicules_dispos)

@admin_bp.route("/conducteur/ajouter", methods=["GET", "POST"])
@login_required
def ajouter_conducteur():
    if current_user.role != 'admin':
        flash("Accès interdit", "danger")
        return redirect(url_for("auth.login"))

    form = ConducteurForm()
    if form.validate_on_submit():
        conducteur = Utilisateur(
            nom=form.nom.data,
            email=form.email.data,
            mot_de_passe=form.mot_de_passe.data,
            role='conducteur',
            actif=True
        )
        db.session.add(conducteur)
        db.session.flush()  # Pour obtenir l'ID du conducteur avant de créer le profil

        conducteur.profil = ConducteurProfil(
            utilisateur_id=conducteur.id,
            adresse=form.adresse.data,
            telephone=form.telephone.data,
            permis_conduit=form.permis_conduit.data,
            date_naissance=form.date_naissance.data
        )
        db.session.add(conducteur.profil)
        try:
            db.session.commit()
            flash("Conducteur ajouté avec succès", "success")
            return redirect(url_for("admin.dashboard"))
        except IntegrityError as e:
            db.session.rollback()
            if "utilisateur_email_key" in str(e.orig):
                flash("Cet email est déjà utilisé.", "danger")
            else:
                flash("Erreur lors de l'ajout du conducteur.", "danger")
    return render_template("admin/ajouter_conducteur.html", form=form)
