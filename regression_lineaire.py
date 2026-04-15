
# Validation de la régression linéaire multiple avec Python
# Auteur : El Yahyaoui Mohamed — Université Paris-Est Créteil
# Outil   : Python (scikit-learn, pandas, matplotlib)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Chargement du fichier Excel
data = pd.read_excel("BD.xlsx")

# Suppression des lignes avec des valeurs manquantes
data = data.dropna(subset=['Age', 'Buts', 'Passes', 'Minutes', 'Valj'])
print("Nombre de lignes après nettoyage :", len(data))

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

# Régression linéaire
model = LinearRegression()
model.fit(X, y)

# Affichage des coefficients
coefficients = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.coef_})
print("\nCoefficients de la régression :")
print(coefficients)
print(f"Intercept : {model.intercept_:.4f}")

# Validation croisée (5-fold)
cv_scores = cross_val_score(model, X, y, cv=5)
print("\nScores de validation croisée :", cv_scores)
print("Moyenne des scores :", cv_scores.mean())
print("Écart-type des scores :", cv_scores.std())

# Visualisation : Prédictions vs Valeurs réelles
y_pred = model.predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, y, color='blue', alpha=0.6, label='Joueurs')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Ligne idéale')
plt.xlabel('Valeurs prédites (M€)')
plt.ylabel('Valeurs réelles (M€)')
plt.title('Prédictions vs Valeurs réelles — Régression linéaire')
plt.legend()
plt.tight_layout()
plt.show()
