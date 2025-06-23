#!/usr/bin/env python3
"""
Script pour créer des données de test dans la base de données
avec des utilisateurs, véhicules et profils sénégalais
"""

from app import create_app, db
from app.models import Utilisateur, ConducteurProfil, Vehicule, VehiculeAssignation, Itineraire
from datetime import date, datetime
from werkzeug.security import generate_password_hash

def create_test_data():
    app = create_app()
    with app.app_context():
        # Supprimer toutes les données existantes
        print("🗑️  Suppression des données existantes...")
        db.drop_all()
        db.create_all()
        
        # 1. Créer un admin
        print("👨‍💼 Création de l'administrateur...")
        admin = Utilisateur(
            nom="Amadou Diallo",
            email="admin@parcauto.sn",
            mot_de_passe="admin123",  # En production, utiliser generate_password_hash()
            role="admin",
            actif=True
        )
        db.session.add(admin)
        
        # 2. Créer des conducteurs avec profils
        print("👨‍✈️ Création des conducteurs...")
        conducteurs_data = [
            {
                "nom": "Mamadou Ndiaye",
                "email": "mndiaye@parcauto.sn",
                "mot_de_passe": "conducteur123",
                "profil": {
                    "adresse": "Dakar Plateau, Rue Mohamed V",
                    "telephone": "771234567",
                    "permis_conduit": "B1234567",
                    "date_naissance": date(1985, 4, 12)
                }
            },
            {
                "nom": "Fatou Diop",
                "email": "fdiop@parcauto.sn",
                "mot_de_passe": "conducteur123",
                "profil": {
                    "adresse": "Parcelles Assainies, Unité 15",
                    "telephone": "782345678",
                    "permis_conduit": "C2345678",
                    "date_naissance": date(1990, 8, 25)
                }
            },
            {
                "nom": "Cheikh Sarr",
                "email": "csarr@parcauto.sn",
                "mot_de_passe": "conducteur123",
                "profil": {
                    "adresse": "Guédiawaye, Cité Millionnaire",
                    "telephone": "773456789",
                    "permis_conduit": "D3456789",
                    "date_naissance": date(1982, 12, 3)
                }
            },
            {
                "nom": "Awa Ba",
                "email": "aba@parcauto.sn",
                "mot_de_passe": "conducteur123",
                "profil": {
                    "adresse": "Pikine, Zone B",
                    "telephone": "784567890",
                    "permis_conduit": "E4567890",
                    "date_naissance": date(1995, 3, 17)
                }
            },
            {
                "nom": "Ibrahima Faye",
                "email": "ifaye@parcauto.sn",
                "mot_de_passe": "conducteur123",
                "profil": {
                    "adresse": "Rufisque, Quartier Keury Kao",
                    "telephone": "775678901",
                    "permis_conduit": "F5678901",
                    "date_naissance": date(1988, 7, 29)
                }
            }
        ]
        
        conducteurs = []
        for data in conducteurs_data:
            conducteur = Utilisateur(
                nom=data["nom"],
                email=data["email"],
                mot_de_passe=data["mot_de_passe"],
                role="conducteur",
                actif=True
            )
            db.session.add(conducteur)
            db.session.flush()  # Pour obtenir l'ID
            
            # Créer le profil conducteur
            profil = ConducteurProfil(
                utilisateur_id=conducteur.id,
                adresse=data["profil"]["adresse"],
                telephone=data["profil"]["telephone"],
                permis_conduit=data["profil"]["permis_conduit"],
                date_naissance=data["profil"]["date_naissance"]
            )
            db.session.add(profil)
            conducteurs.append(conducteur)
        
        # 3. Créer des véhicules
        print("🚗 Création des véhicules...")
        vehicules_data = [
            {
                "marque": "Toyota",
                "modele": "Corolla",
                "annee": 2020,
                "immatriculation": "DK-2020-AA",
                "couleur_exterieure": "Blanc",
                "couleur_interieure": "Noir",
                "type_carburant": "essence",
                "transmission": "automatique",
                "puissance": 140,
                "kilometrage": 45000,
                "disponible": True
            },
            {
                "marque": "Peugeot",
                "modele": "208",
                "annee": 2019,
                "immatriculation": "DK-2019-BB",
                "couleur_exterieure": "Rouge",
                "couleur_interieure": "Gris",
                "type_carburant": "diesel",
                "transmission": "manuelle",
                "puissance": 110,
                "kilometrage": 62000,
                "disponible": True
            },
            {
                "marque": "Renault",
                "modele": "Duster",
                "annee": 2021,
                "immatriculation": "DK-2021-CC",
                "couleur_exterieure": "Noir",
                "couleur_interieure": "Beige",
                "type_carburant": "essence",
                "transmission": "automatique",
                "puissance": 115,
                "kilometrage": 25000,
                "disponible": True
            },
            {
                "marque": "Hyundai",
                "modele": "i10",
                "annee": 2018,
                "immatriculation": "DK-2018-DD",
                "couleur_exterieure": "Bleu",
                "couleur_interieure": "Noir",
                "type_carburant": "essence",
                "transmission": "manuelle",
                "puissance": 87,
                "kilometrage": 78000,
                "disponible": True
            },
            {
                "marque": "Volkswagen",
                "modele": "Golf",
                "annee": 2022,
                "immatriculation": "DK-2022-EE",
                "couleur_exterieure": "Gris",
                "couleur_interieure": "Noir",
                "type_carburant": "hybride",
                "transmission": "automatique",
                "puissance": 150,
                "kilometrage": 15000,
                "disponible": True
            }
        ]
        
        vehicules = []
        for data in vehicules_data:
            vehicule = Vehicule(**data)
            db.session.add(vehicule)
            vehicules.append(vehicule)
        
        db.session.flush()  # Pour obtenir les IDs des véhicules
        
        # 4. Créer quelques assignations véhicule-conducteur
        print("🔗 Création des assignations...")
        assignations_data = [
            {"conducteur": conducteurs[0], "vehicule": vehicules[0]},
            {"conducteur": conducteurs[1], "vehicule": vehicules[1]},
            {"conducteur": conducteurs[2], "vehicule": vehicules[2]},
        ]
        
        for data in assignations_data:
            assignation = VehiculeAssignation(
                conducteur_id=data["conducteur"].id,
                vehicule_id=data["vehicule"].id,
                date_debut=date.today(),
                active=True
            )
            db.session.add(assignation)
            # Marquer le véhicule comme non disponible
            data["vehicule"].disponible = False
        
        # 5. Créer quelques itinéraires
        print("🗺️  Création des itinéraires...")
        itineraires_data = [
            {
                "conducteur_id": conducteurs[0].id,
                "vehicule_id": vehicules[0].id,
                "date_trajet": date(2024, 12, 20),
                "lieu_depart": "Dakar Plateau",
                "lieu_arrivee": "Aéroport LSS",
                "distance_km": 25.5,
                "duree_minutes": 45,
                "polyline": '[[14.6928, -17.4467], [14.7392, -17.4902]]'
            },
            {
                "conducteur_id": conducteurs[1].id,
                "vehicule_id": vehicules[1].id,
                "date_trajet": date(2024, 12, 21),
                "lieu_depart": "Parcelles Assainies",
                "lieu_arrivee": "Sandaga",
                "distance_km": 18.2,
                "duree_minutes": 35,
                "polyline": '[[14.7644, -17.3653], [14.6737, -17.4541]]'
            },
            {
                "conducteur_id": conducteurs[2].id,
                "vehicule_id": vehicules[2].id,
                "date_trajet": date(2024, 12, 22),
                "lieu_depart": "Guédiawaye",
                "lieu_arrivee": "Grand Dakar",
                "distance_km": 22.8,
                "duree_minutes": 50,
                "polyline": '[[14.7697, -17.4075], [14.7158, -17.4731]]'
            }
        ]
        
        for data in itineraires_data:
            itineraire = Itineraire(**data)
            db.session.add(itineraire)
        
        # 6. Sauvegarder tout
        print("💾 Sauvegarde en base de données...")
        db.session.commit()
        
        print("\n✅ Données de test créées avec succès !")
        print("\n📋 Comptes créés :")
        print("👨‍💼 Admin: admin@parcauto.sn / admin123")
        print("👨‍✈️ Conducteurs:")
        for conducteur in conducteurs:
            print(f"   - {conducteur.nom}: {conducteur.email} / conducteur123")
        
        print(f"\n🚗 {len(vehicules)} véhicules créés")
        print(f"🔗 {len(assignations_data)} assignations créées")
        print(f"🗺️  {len(itineraires_data)} itinéraires créés")

if __name__ == "__main__":
    create_test_data()
