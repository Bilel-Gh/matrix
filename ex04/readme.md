## Concept
3 façons différentes de mesurer la "taille" d'un vecteur.

C'est simplement différentes façons de mesurer la longueur d'une flèche :

- Norme 1 : Tu marches le long des rues d'une ville (pas de diagonales !)
- Norme 2 : Tu mesures directement à vol d'oiseau
- Norme infinie : Tu regardes le plus grand nombre parmi les composantes

## Les 3 normes

### Norme 1 (Manhattan) 🏙️
||[3, 4]||₁ = |3| + |4| = 7
**Analogie** : distance en ville (suivre les rues)

### Norme 2 (Euclidienne) 🐦
||[3, 4]||₂ = √(3² + 4²) = 5
**Analogie** : distance à vol d'oiseau (ligne droite)

### Norme ∞ (Infinie) 📏
||[3, 4]||∞ = max(3, 4) = 4
**Analogie** : plus grande coordonnée

## Exemple pratique
De chez toi [0,0] au supermarché [3,4] :

En ville : 7 blocs (3 → + 4 ↑)
À vol d'oiseau : 5 km (hypoténuse)
Plus grande distance : 4 km (axe principal)


## Applications
- **GPS** : calcul d'itinéraires
- **Jeux** : portée d'attaque, zones d'effet
- **Machine Learning** : distance entre données
- **Optimisation** : contraintes de performance
