from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM
from flask_login import UserMixin

from . import db

# Définition des types ENUM PostgreSQL
role_enum = ENUM('admin', 'conducteur', name='role_type', create_type=False)
carburant_enum = ENUM('essence', 'diesel', 'electrique', 'hybride', name='carburant_type', create_type=False)
transmission_enum = ENUM('manuelle', 'automatique', name='transmission_type', create_type=False)

# === UTILISATEUR ===
class Utilisateur(db.Model,UserMixin):
    __tablename__ = "utilisateur"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(role_enum, nullable=False)
    actif = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profil = db.relationship("ConducteurProfil", backref="utilisateur", uselist=False)
    vehicule_assignations = db.relationship("VehiculeAssignation", backref="conducteur_utilisateur")
    itineraires = db.relationship("Itineraire", backref="conducteur_utilisateur")

# === PROFIL CONDUCTEUR ===
class ConducteurProfil(db.Model):
    __tablename__ = "conducteur_profil"
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey("utilisateur.id", ondelete="CASCADE"), nullable=False)
    adresse = db.Column(db.Text)
    telephone = db.Column(db.String(20))
    permis_conduit = db.Column(db.String(50))
    date_naissance = db.Column(db.Date)

# === VEHICULE ===
class Vehicule(db.Model):
    __tablename__ = "vehicule"
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(100))
    modele = db.Column(db.String(100))
    annee = db.Column(db.Integer)
    immatriculation = db.Column(db.String(50), unique=True)
    couleur_exterieure = db.Column(db.String(50))
    couleur_interieure = db.Column(db.String(50))
    type_carburant = db.Column(carburant_enum)
    transmission = db.Column(transmission_enum)
    puissance = db.Column(db.Integer)
    kilometrage = db.Column(db.Integer)
    disponible = db.Column(db.Boolean, default=True)

    assignations = db.relationship("VehiculeAssignation", backref="vehicule")
    itineraires = db.relationship("Itineraire", backref="vehicule")

# === ASSIGNATION VEHICULE ⇔ CONDUCTEUR ===
class VehiculeAssignation(db.Model):
    __tablename__ = "vehicule_assignation"
    id = db.Column(db.Integer, primary_key=True)
    conducteur_id = db.Column(db.Integer, db.ForeignKey("utilisateur.id"))
    vehicule_id = db.Column(db.Integer, db.ForeignKey("vehicule.id"))
    date_debut = db.Column(db.Date)
    date_fin = db.Column(db.Date)
    active = db.Column(db.Boolean, default=True)

# === ITINERAIRE ===
class Itineraire(db.Model):
    __tablename__ = "itineraire"
    id = db.Column(db.Integer, primary_key=True)
    conducteur_id = db.Column(db.Integer, db.ForeignKey("utilisateur.id"))
    vehicule_id = db.Column(db.Integer, db.ForeignKey("vehicule.id"))
    date_trajet = db.Column(db.Date)
    lieu_depart = db.Column(db.Text)
    lieu_arrivee = db.Column(db.Text)
    distance_km = db.Column(db.Float)
    duree_minutes = db.Column(db.Integer)
    polyline = db.Column(db.Text)
