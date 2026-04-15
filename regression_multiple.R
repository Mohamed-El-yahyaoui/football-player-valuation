# ============================================================
# Analyse économétrique des déterminants de la valeur marchande
# des joueurs de football en Europe
# Auteur : El Yahyaoui Mohamed — Université Paris-Est Créteil
# Outil   : R Studio
# ============================================================

# Étape 1 : Définir le répertoire de travail
setwd("C:/Users/moham/Desktop/base")  # À adapter selon votre machine

# Étape 2 : Charger les données
data <- read.csv2("BD.csv", header = TRUE, stringsAsFactors = TRUE, encoding = "latin1")

# Étape 3 : Vérifier la structure des données
print(str(data))

# Étape 4 : Nettoyer et convertir les types de données
data$Valeur  <- as.numeric(gsub("M", "", data$Valeur))
data$Age     <- as.numeric(as.character(data$Age))
data$Buts    <- as.numeric(as.character(data$Buts))
data$Passes  <- as.numeric(as.character(data$Passes))
data$Minutes <- as.numeric(as.character(data$Minutes))

# Étape 5 : Créer la variable Âge centré à 26 ans (pic de carrière)
data$Age_centre <- data$Age - 26

# Étape 6 : Créer les variables binaires
# Grand Club (1) ou Petit Club (0)
grands_clubs <- c("PSG", "Manchester City", "Real Madrid", "Liverpool",
                  "Manchester United", "Bayern Munich", "Inter Milan",
                  "Arsenal", "Tottenham", "Barcelone", "Atletico Madrid",
                  "Bayer Leverkusen", "AS Roma", "Lazio")
data$GrandClub <- ifelse(data$Club %in% grands_clubs, 1, 0)

# Grande nation de football (1) ou Non (0)
grands_pays <- c("France", "Norvege", "Angleterre", "Pays-Bas", "Belgique",
                 "Bresil", "Egypte", "Portugal", "Allemagne", "Italie",
                 "Argentine", "Espagne", "Uruguay", "Maroc")
data$GrandPays <- ifelse(data$Nationalite %in% grands_pays, 1, 0)

# Position offensive (1) ou défensive/gardien (0)
data$PositionBinaire <- ifelse(data$Position %in% c("Attaquant", "Milieu"), 1, 0)

# Étape 7 : Régression multiple
# Valeur = f(Age, Age², Buts, Passes, Minutes, Position, Club, Nationalité)
model <- lm(Valeur ~ Age_centre + I(Age_centre^2) + Buts + Passes + Minutes +
              PositionBinaire + GrandClub + GrandPays, data = data)

# Étape 8 : Afficher les résultats
summary(model)

# ============================================================
# Tests statistiques
# ============================================================

# Test de significativité globale (Fisher)
# H0 : le modèle n'est pas globalement significatif
# H1 : au moins un coefficient est différent de 0
# Fc = (R²/k-1) / ((1-R²)/(N-k))  avec R²=0.6751, k=7, N-k=88
# Fc = 30.47 > F(6,88)=2.20 à 5% → on rejette H0

# Test de Breusch-Pagan (homoscédasticité)
# H0 : homoscédasticité   H1 : hétéroscédasticité
# BPc = N × R²_ajusté = 95 × 0.6445 = 61.23 > χ²(5, 0.95)=14.07 → on rejette H0

# Test de Breusch-Godfrey (autocorrélation)
# H0 : pas d'autocorrélation   H1 : autocorrélation
# BGc = 94 × 0.6445 = 60.58 > χ²(1, 0.95)=3.84 → on rejette H0
