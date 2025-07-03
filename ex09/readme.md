## Concept
"Retourner" une matrice : les lignes deviennent des colonnes.

Imagine que tu as un tableau de nombres. La transposée, c'est comme si tu faisais pivoter ce tableau pour que les lignes deviennent des colonnes et les colonnes deviennent des lignes.

## Applications pratiques

### Optimisation calculs 💻
# Souvent plus rapide de calculer :
A.transpose() × B
# que directement A × B (selon la taille)
Changement de perspective 🔄

Base de données : lignes ↔ colonnes
Images : rotation de 90° + miroir
Machine Learning : réorganisation des données

Algèbre linéaire avancée

Matrices symétriques : A = Aᵀ
Matrices orthogonales : A⁻¹ = Aᵀ

Point technique
🔄 Double transposition : (Aᵀ)ᵀ = A
⚡ Propriété importante : (AB)ᵀ = BᵀAᵀ (ordre inversé !)
