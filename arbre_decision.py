# ============================================================
# Modèle d'arbre de décision pour estimer la valeur marchande
# des joueurs de football
# Auteur : El Yahyaoui Mohamed — Université Paris-Est Créteil
# Outil   : Python (scikit-learn, pandas)
# ============================================================

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

# Chargement du fichier Excel
data = pd.read_excel("BD.xlsx")

# Suppression des lignes avec des valeurs manquantes
data = data.dropna(subset=['Age', 'Buts', 'Passes', 'Minutes', 'Valj'])

# Variable Âge centré à 26 ans
data['Age_centre']    = data['Age'] - 26
data['Age_centre**2'] = data['Age_centre'] ** 2

# Variables binaires
grands_clubs = ["PSG", "Manchester City", "Real Madrid", "Liverpool",
                "Manchester United", "Bayern Munich", "Inter Milan",
                "Arsenal", "Tottenham", "Barcelone", "Atletico Madrid",
                "Bayer Leverkusen", "AS Roma", "Lazio"]
data['GrandClub'] = data['Club'].isin(grands_clubs).astype(int)

grands_pays = ["France", "Norvege", "Angleterre", "Pays-Bas", "Belgique",
               "Bresil", "Egypte", "Portugal", "Allemagne", "Italie",
               "Argentine", "Espagne", "Uruguay", "Maroc"]
data['GrandPays'] = data['Nationalite'].isin(grands_pays).astype(int)

data['PositionBinaire'] = data['Position'].isin(['Attaquant', 'Milieu']).astype(int)

# Préparation des variables
X = data[['Age_centre', 'Age_centre**2', 'Buts', 'Passes', 'Minutes',
          'PositionBinaire', 'GrandClub', 'GrandPays']]
y = data['Valj']

# Arbre de décision
model_tree = DecisionTreeRegressor(random_state=42)
model_tree.fit(X, y)

# Importance des variables
feature_importance = pd.DataFrame({
    'Variable'  : X.columns,
    'Importance': model_tree.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nImportance des variables dans l'arbre de décision :")
print(feature_importance.to_string(index=False))

# Validation croisée (5-fold)
cv_scores = cross_val_score(model_tree, X, y, cv=5)
print("\nScores de validation croisée (Arbre de décision) :", cv_scores)
print("Moyenne des scores :", cv_scores.mean())
print("Écart-type des scores  :", cv_scores.std())

# ============================================================
# Résultats obtenus
# ------------------------------------------------------------
# Variable         Importance
# Buts               0.310
# Passes             0.150
# Age_centre         0.125
# GrandClub          0.110
# Minutes            0.090
# Age_centre**2      0.080
# GrandPays          0.080
# PositionBinaire    0.055
# ============================================================
