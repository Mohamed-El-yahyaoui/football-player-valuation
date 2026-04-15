# Analyse des déterminants de la valeur marchande des joueurs de football 

Projet Individuel Tutoré — Licence Économie & Gestion (L3)  
Université Paris-Est Créteil (UPEC)

---

## Objectif

Ce projet analyse les facteurs qui influencent la **valeur marchande des joueurs de football** dans les 5 grands championnats européens (Premier League, La Liga, Serie A, Bundesliga, Ligue 1) sur la période 2015–2024.

---

## Données

- **Joueurs** issus des 5 grands championnats européens (saison 2023-2024)
- Sources : Transfermarkt, Opta, CIES Football Observatory
- Variables : âge, buts, passes décisives, minutes jouées, poste, club, nationalité

---

## Fichiers

| Fichier | Description |
|---|---|
| `regression_multiple.R` | Régression multiple sous R Studio (modèle principal) |
| `regression_lineaire.py` | Validation de la régression avec Python (scikit-learn) |
| `arbre_decision.py` | Arbre de décision pour capturer les effets non linéaires |

---

## Principaux résultats

| Variable | Coefficient (M€) |
|---|---|
| Buts | +2,56 par but |
| Passes décisives | +2,04 par passe |
| Âge (écart vs 26 ans) | −5,56 par année |
| Grand pays de football | +11,78 |
| Grand club | +3,98 |

**R² ajusté : 0,675** — le modèle explique 67,5 % de la variance des valeurs marchandes.

---

## Outils utilisés

- **R / RStudio** — régressions économétriques
- **Python** — scikit-learn, pandas, matplotlib

---

## Auteur

**El Yahyaoui Mohamed**
