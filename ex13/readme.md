## Concept
Nombre de "dimensions indépendantes" que conserve une transformation.

C'est comme compter combien de directions différentes ta transformation peut prendre. Plus le rang est grand, plus ta transformation peut faire des choses différentes !

Imagine que tu dessines. Tu peux faire :

- Une ligne : c'est rang 1, tu ne peux bouger que dans une direction
- Un dessin sur une feuille plate : c'est rang 2, tu peux bouger dans deux directions (gauche/droite et haut/bas)
- Un objet en 3D comme une sculpture : c'est rang 3, tu peux bouger dans toutes les directions

Le rang nous dit donc combien de dimensions "utiles" nous avons vraiment. Par exemple, si tu dessines une ligne sur une feuille, même si la feuille est en 2D, ton dessin n'utilise qu'une dimension donc rang 1.

## Interprétation visuelle
Matrice 3×3 :

Rang 3 → préserve l'espace 3D complet 📦
Rang 2 → écrase en plan 2D 📄
Rang 1 → écrase en ligne 1D 📏
Rang 0 → écrase en point 📍

## Applications pratiques
Compression d'images 🖼️
Machine Learning 🤖

Réduction de dimensions : simplifier les données
Détection de redondance : variables inutiles
Analyse en composantes principales (PCA)

Analyse de systèmes 🔍

Rang < n → système sous-déterminé (plusieurs solutions)
Rang = n → système bien posé (solution unique)

Point technique
📏 Limite : rang ≤ min(lignes, colonnes)
🎯 Calcul : nombre de lignes non-nulles après forme échelonnée
