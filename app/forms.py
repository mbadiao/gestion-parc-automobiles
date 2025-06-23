from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, DateField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

# ==== Formulaire de Connexion ====
class ConnexionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField("Mot de passe", validators=[DataRequired()])
    se_souvenir = BooleanField("Se souvenir de moi")
    submit = SubmitField("Connexion")

# ==== Formulaire de Création d’un Conducteur ====
class ConducteurForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=6)])
    mot_de_passe2 = PasswordField("Confirmer", validators=[EqualTo('mot_de_passe')])
    adresse = TextAreaField("Adresse")
    telephone = StringField("Téléphone")
    permis_conduit = StringField("Permis de conduire")
    date_naissance = DateField("Date de naissance", format='%Y-%m-%d')
    submit = SubmitField("Créer le conducteur")

# ==== Formulaire de Véhicule ====
class VehiculeForm(FlaskForm):
    marque = StringField("Marque", validators=[DataRequired()])
    modele = StringField("Modèle", validators=[DataRequired()])
    annee = IntegerField("Année", validators=[DataRequired()])
    immatriculation = StringField("Immatriculation", validators=[DataRequired()])
    couleur_exterieure = StringField("Couleur extérieure")
    couleur_interieure = StringField("Couleur intérieure")
    type_carburant = SelectField("Type de carburant", choices=[
        ('essence', 'Essence'),
        ('diesel', 'Diesel'),
        ('electrique', 'Électrique'),
        ('hybride', 'Hybride')
    ], validators=[DataRequired()])
    transmission = SelectField("Transmission", choices=[
        ('manuelle', 'Manuelle'),
        ('automatique', 'Automatique')
    ], validators=[DataRequired()])
    puissance = IntegerField("Puissance")
    kilometrage = IntegerField("Kilométrage")
    description = TextAreaField("Description", validators=[Optional()])
    disponible = BooleanField("Disponible", default=True)
    submit = SubmitField("Enregistrer le véhicule")

# ==== Formulaire d’Assignation d’un Véhicule à un Conducteur ====
class AssignationForm(FlaskForm):
    conducteur_id = SelectField("Conducteur", coerce=int, validators=[DataRequired()])
    vehicule_id = SelectField("Véhicule", coerce=int, validators=[DataRequired()])
    date_debut = DateField("Date de début", format='%Y-%m-%d', validators=[Optional()])
    date_fin = DateField("Date de fin", format='%Y-%m-%d', validators=[Optional()])
    active = BooleanField("Active", default=True)
    submit = SubmitField("Assigner")

# ==== Formulaire d’Itinéraire ====
class ItineraireForm(FlaskForm):
    lieu_depart = StringField("Lieu de départ", validators=[DataRequired()])
    lieu_arrivee = StringField("Lieu d’arrivée", validators=[DataRequired()])
    date_trajet = DateField("Date du trajet", format='%Y-%m-%d', validators=[DataRequired()])
    distance_km = FloatField("Distance (km)", validators=[Optional()])
    duree_minutes = IntegerField("Durée (minutes)", validators=[Optional()])
    polyline = TextAreaField("Polyline", validators=[Optional()])
    submit = SubmitField("Soumettre trajet")
