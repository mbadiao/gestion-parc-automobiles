# 🧪 Guide de test de l'application Gestion Parc Automobiles

## 🎯 Données de test créées

L'application a été initialisée avec des données de test réalistes utilisant des noms et adresses sénégalais.

### 👨‍💼 Compte Administrateur
- **Email**: `admin@parcauto.sn`
- **Mot de passe**: `admin123`
- **Nom**: Amadou Diallo

### 👨‍✈️ Comptes Conducteurs
| Nom | Email | Mot de passe | Téléphone | Adresse |
|-----|-------|--------------|-----------|---------|
| Mamadou Ndiaye | mndiaye@parcauto.sn | conducteur123 | 771234567 | Dakar Plateau, Rue Mohamed V |
| Fatou Diop | fdiop@parcauto.sn | conducteur123 | 782345678 | Parcelles Assainies, Unité 15 |
| Cheikh Sarr | csarr@parcauto.sn | conducteur123 | 773456789 | Guédiawaye, Cité Millionnaire |
| Awa Ba | aba@parcauto.sn | conducteur123 | 784567890 | Pikine, Zone B |
| Ibrahima Faye | ifaye@parcauto.sn | conducteur123 | 775678901 | Rufisque, Quartier Keury Kao |

### 🚗 Véhicules créés
1. **Toyota Corolla 2020** (DK-2020-AA) - Blanc - ✅ Attribué à Mamadou
2. **Peugeot 208 2019** (DK-2019-BB) - Rouge - ✅ Attribué à Fatou  
3. **Renault Duster 2021** (DK-2021-CC) - Noir - ✅ Attribué à Cheikh
4. **Hyundai i10 2018** (DK-2018-DD) - Bleu - 🟢 Disponible
5. **Volkswagen Golf 2022** (DK-2022-EE) - Gris - 🟢 Disponible

### 🗺️ Itinéraires créés
- **Mamadou**: Dakar Plateau → Aéroport LSS (25.5 km)
- **Fatou**: Parcelles Assainies → Sandaga (18.2 km)
- **Cheikh**: Guédiawaye → Grand Dakar (22.8 km)

## 🧪 Scénarios de test

### 1. Test Administrateur
1. **Connexion**: `admin@parcauto.sn` / `admin123`
2. **Dashboard**: Voir la liste des véhicules et conducteurs
3. **Ajout véhicule**: Tester le formulaire multi-étapes
4. **Attribution**: Attribuer un véhicule disponible à Awa ou Ibrahima
5. **Itinéraire**: Créer un itinéraire pour un véhicule attribué

### 2. Test Conducteur
1. **Connexion**: `mndiaye@parcauto.sn` / `conducteur123`
2. **Dashboard**: Voir les trajets et la carte interactive
3. **Sélection trajet**: Cliquer sur un trajet pour voir l'itinéraire sur la carte

### 3. Test Fonctionnalités
- ✅ **Authentification**: Login/logout
- ✅ **Gestion véhicules**: CRUD véhicules avec formulaire progressif
- ✅ **Attribution**: Assigner véhicules aux conducteurs
- ✅ **Conducteurs**: Ajouter des conducteurs avec formulaire multi-étapes
- ✅ **Itinéraires**: Créer et visualiser les trajets sur carte
- ✅ **Cartes interactives**: OpenStreetMap avec tracé de routes
- ✅ **Interface responsive**: Design adapté mobile/desktop

## 🚀 Lancement de l'application

1. **Activer l'environnement virtuel**:
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```

2. **Lancer l'application**:
   ```bash
   python main.py
   ```

3. **Accéder à l'application**:
   - URL: http://127.0.0.1:5000
   - Utiliser les comptes ci-dessus pour tester

## 🔄 Réinitialiser les données

Pour recréer les données de test :
```bash
python create_test_data.py
```

## 🎨 Fonctionnalités UI testées
- **Thème sombre**: Interface moderne avec couleurs violettes/bleues
- **Formulaires progressifs**: Multi-étapes avec navigation
- **Tableaux interactifs**: Tri, filtres, actions par ligne
- **Cartes OpenStreetMap**: Traçage d'itinéraires interactif
- **Responsive design**: Adaptation mobile et desktop
- **Icônes**: Lucide et FontAwesome intégrés

## 📱 Tests mobiles
L'interface est responsive et testable sur :
- Smartphones (< 600px)
- Tablettes (600-900px)  
- Desktop (> 900px)

---

**Note**: Les mots de passe sont volontairement simples pour les tests. En production, utiliser des mots de passe sécurisés et du hachage.
