# PRÉSENTATION POWERPOINT - GESTION DE PARC AUTOMOBILE

## SLIDE 1 - TITRE
**SYSTÈME DE GESTION DE PARC AUTOMOBILE**
Développement d'une application web complète
*Réalisé avec Flask, SQLAlchemy et PostgreSQL*

---

## SLIDE 2 - CONTEXTE
**CONTEXTE DU PROJET**

• **Besoin** : Digitalisation de la gestion de flotte véhicules
• **Secteur** : Transport et logistique au Sénégal
• **Utilisateurs** : Administrateurs et conducteurs
• **Objectif** : Optimiser l'attribution et le suivi des véhicules

---

## SLIDE 3 - PROBLÉMATIQUE
**PROBLÉMATIQUE IDENTIFIÉE**

**Défis actuels :**
• Gestion manuelle des assignations véhicule-conducteur
• Absence de traçabilité des itinéraires
• Difficulté de suivi en temps réel
• Manque de visibilité sur la disponibilité des véhicules

**Solution proposée :**
Application web centralisée avec interface intuitive

---

## SLIDE 4 - ARCHITECTURE TECHNIQUE
**STACK TECHNOLOGIQUE**

**Backend :**
• Flask (Framework Python)
• SQLAlchemy (ORM)
• PostgreSQL (Base de données)

**Frontend :**
• HTML5, CSS3, JavaScript
• Leaflet.js (Cartographie)
• Design responsive

**Sécurité :**
• Authentification utilisateur
• Gestion des rôles (Admin/Conducteur)

---

## SLIDE 5 - MODÈLE DE DONNÉES
**STRUCTURE DE LA BASE DE DONNÉES**

**Entités principales :**
• **Utilisateur** : Profils admin et conducteurs
• **Véhicule** : Caractéristiques complètes
• **Assignation** : Liaison véhicule-conducteur
• **Itinéraire** : Trajets avec géolocalisation

**Relations :**
• 1 Conducteur ↔ N Véhicules
• 1 Véhicule ↔ N Itinéraires

---

## SLIDE 6 - PAGE DE CONNEXION
**INTERFACE D'AUTHENTIFICATION**

*[Capture d'écran de la page de login]*

**Fonctionnalités :**
• Connexion sécurisée par email/mot de passe
• Design moderne avec thème sombre
• Redirection selon le rôle utilisateur
• Validation des données en temps réel

---

## SLIDE 7 - DASHBOARD ADMINISTRATEUR
**TABLEAU DE BORD ADMIN**

*[Capture d'écran du dashboard admin]*

**Vue d'ensemble :**
• Gestion centralisée de tous les éléments
• Onglets : Conducteurs, Véhicules, Assignations
• Actions rapides : Ajouter, Modifier, Supprimer
• Interface intuitive avec navigation fluide

---

## SLIDE 8 - GESTION DES CONDUCTEURS
**MODULE CONDUCTEURS**

*[Capture d'écran de la liste des conducteurs]*

**Fonctionnalités :**
• Liste complète avec informations détaillées
• Ajout de nouveaux profils conducteurs
• Données personnelles et permis de conduire
• Statut actif/inactif

---

## SLIDE 9 - FORMULAIRE CONDUCTEUR
**AJOUT DE CONDUCTEUR**

*[Capture d'écran du formulaire multi-étapes]*

**Processus en 3 étapes :**
• **Étape 1** : Informations personnelles
• **Étape 2** : Coordonnées et contact
• **Étape 3** : Permis et validation
• Navigation intuitive avec indicateurs visuels

---

## SLIDE 10 - GESTION DES VÉHICULES
**MODULE VÉHICULES**

*[Capture d'écran de la liste des véhicules]*

**Caractéristiques :**
• Catalogue complet du parc automobile
• Informations techniques détaillées
• Statut de disponibilité en temps réel
• Actions : Modifier, Supprimer, Assigner

---

## SLIDE 11 - FORMULAIRE VÉHICULE
**AJOUT DE VÉHICULE**

*[Capture d'écran du formulaire véhicule]*

**Données collectées :**
• Identité : Marque, modèle, année
• Technique : Moteur, transmission, carburant
• Administratif : Immatriculation, couleurs
• Validation en temps réel

---

## SLIDE 12 - ATTRIBUTION VÉHICULE
**ASSIGNATION VÉHICULE-CONDUCTEUR**

*[Capture d'écran de l'attribution]*

**Processus d'attribution :**
• Sélection du conducteur
• Choix du véhicule disponible
• Définition des dates d'attribution
• Badges visuels de disponibilité

---

## SLIDE 13 - CRÉATION D'ITINÉRAIRE
**PLANIFICATION DE TRAJETS**

*[Capture d'écran du formulaire itinéraire - Étape 1]*

**Étape 1 - Informations temporelles :**
• Sélection de la date du trajet
• Interface calendrier intuitive
• Validation des dates
• Navigation par étapes

---

## SLIDE 14 - DÉFINITION DES LIEUX
**SAISIE DES DESTINATIONS**

*[Capture d'écran du formulaire itinéraire - Étape 2]*

**Étape 2 - Localisation :**
• Points de départ et d'arrivée
• Saisie textuelle descriptive
• Exemples contextualisés (Sénégal)
• Icônes visuelles d'orientation

---

## SLIDE 15 - CARTOGRAPHIE INTERACTIVE
**GÉOLOCALISATION PRÉCISE**

*[Capture d'écran de la carte Leaflet]*

**Étape 3 - Carte interactive :**
• Sélection de points sur carte OpenStreetMap
• Marqueurs distinctifs (départ/arrivée)
• Calcul automatique d'itinéraire
• Affichage distance et durée

---

## SLIDE 16 - VALIDATION ITINÉRAIRE
**RÉCAPITULATIF ET CONFIRMATION**

*[Capture d'écran du récapitulatif]*

**Étape 4 - Validation :**
• Récapitulatif complet des informations
• Vérification des données saisies
• Métriques calculées (distance, temps)
• Validation finale

---

## SLIDE 17 - DASHBOARD CONDUCTEUR
**INTERFACE CONDUCTEUR**

*[Capture d'écran du dashboard conducteur]*

**Vue conducteur :**
• Visualisation des itinéraires assignés
• Carte des trajets planifiés
• Informations véhicule attribué
• Interface simplifiée et claire

---

## SLIDE 18 - SYSTÈME DE NOTIFICATIONS
**RETOURS UTILISATEUR**

*[Capture d'écran des notifications]*

**Notifications intelligentes :**
• Messages de succès, erreur, information
• Disparition automatique (5 secondes)
• Design harmonisé avec le thème
• Feedback temps réel

---

## SLIDE 19 - DESIGN RESPONSIVE
**ADAPTABILITÉ MOBILE**

*[Captures d'écran mobile/desktop]*

**Responsive Design :**
• Adaptation automatique aux écrans
• Navigation optimisée mobile
• Préservation de l'expérience utilisateur
• Tests sur différentes résolutions

---

## SLIDE 20 - DONNÉES DE TEST
**ENVIRONNEMENT DE DÉMONSTRATION**

**Jeu de données réalistes :**
• Profils d'utilisateurs sénégalais
• Véhicules variés (particuliers, utilitaires)
• Itinéraires contextualisés (Dakar, régions)
• Scénarios d'usage complets

---

## SLIDE 21 - SÉCURITÉ ET PERFORMANCE
**ASPECTS TECHNIQUES**

**Sécurité :**
• Chiffrement des mots de passe
• Sessions sécurisées
• Validation côté serveur
• Protection CSRF

**Performance :**
• Optimisation des requêtes SQL
• Cache des données statiques
• Chargement asynchrone

---

## SLIDE 22 - ÉVOLUTIONS FUTURES
**PERSPECTIVES D'AMÉLIORATION**

**Fonctionnalités à venir :**
• Notifications push en temps réel
• API mobile native
• Rapports et analytics avancés
• Intégration GPS temps réel
• Module de maintenance préventive

---

## SLIDE 23 - CONCLUSION
**BILAN DU PROJET**

**Objectifs atteints :**
✓ Application web fonctionnelle complète
✓ Interface utilisateur moderne et intuitive
✓ Gestion complète du parc automobile
✓ Cartographie interactive intégrée

**Impact :**
• Digitalisation réussie du processus
• Amélioration de l'efficacité opérationnelle
• Base solide pour évolutions futures
