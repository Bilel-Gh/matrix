## Concept
Somme des éléments sur la diagonale principale.

C'est super simple ! Tu prends une matrice carrée et tu additionnes tous les nombres qui sont sur la diagonale (du coin en haut à gauche au coin en bas à droite).

## Calcul simple
Matrix = [2  1  0]    Trace = 2 + 5 + 8 = 15
		[3  5  7]            ↑   ↑   ↑
		[1  2  8]        	 diagonale

## Signification géométrique
La trace indique comment la transformation affecte le "volume" global :
- **Trace > 0** : expansion générale
- **Trace < 0** : contraction générale
- **Trace = 0** : conservation du volume

## Exemple concret
```python
# Mise à l'échelle uniforme ×2
scale_2x = [[2, 0, 0],
            [0, 2, 0],
            [0, 0, 2]]
# Trace = 6 → volume multiplié par 8 (2³)
Applications

Analyse de stabilité : systèmes dynamiques
Optimisation : propriétés des transformations
Physique : conservation d'énergie
Statistics : variance totale

Point technique
✨ Propriété additive : tr(A + B) = tr(A) + tr(B)
🔢 Invariant : tr(AB) = tr(BA)
