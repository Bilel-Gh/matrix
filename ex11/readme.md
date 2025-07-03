## Concept
Un nombre magique qui dit si une transformation peut être "annulée".

C'est comme mesurer comment une transformation change l'espace. Si le déterminant est 0, c'est comme si tu écrasais l'espace en le rendant plus plat. S'il est positif ou négatif, ça te dit si la transformation retourne l'espace ou pas.

Le déterminant représente géométriquement le facteur par lequel votre transformation linéaire change les aires (en 2D) ou les volumes (en 3D).

Par exemple :

Imagine que tu as un ballon. Quand tu appliques une **transformation** avec une matrice :

- Si le déterminant est 2, ton ballon devient deux fois plus gros (la transformation double l'aire/volume)
- Si le déterminant est 1/2 (0.5), ton ballon devient deux fois plus petit ( transformation réduit l'aire/volume de moitié)
- Si le déterminant est négatif, ton ballon est retourné comme une chaussette ( transformation inverse l'orientation de l'espace)
- Si le déterminant est 0, ton ballon est complètement aplati comme une crêpe

## Interprétation simple
det = 0  → Transformation "écrase" l'espace ❌ (irréversible)
det ≠ 0  → Transformation préserve l'espace ✅ (réversible)
det > 0  → Orientation préservée ➡️
det < 0  → Orientation inversée (effet miroir) ⤴️

## Signification géométrique
**|det|** = facteur de changement d'aire (2D) ou volume (3D)

# Matrice qui double les tailles
scale_2x = [[2, 0],
            [0, 2]]
# det = 4 → aire multipliée par 4 !
Cas particuliers importants
det = 0 💥
# Matrice qui "écrase" en ligne
flatten = [[1, 1],
           [1, 1]]
# det = 0 → tout devient sur une ligne !
det = 1 ✨

Transformation qui préserve aire/volume
Rotations pures, réflexions

Applications

Existence de solutions : système Ax = b
Calculs d'aires/volumes : géométrie
Détection de singularités : matrices problématiques

Point technique
🎯 Limité à 4×4 dans ce projet (simplicité)
⚡ Méthodes différentes par taille de matrice
