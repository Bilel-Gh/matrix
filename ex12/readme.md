## Concept
Trouver la transformation qui "annule" une autre transformation.

C'est comme avoir une machine qui défait ce qu'une autre machine a fait. Si une matrice tourne quelque chose de 45 degrés, son inverse le tourne de -45 degrés pour revenir au début.

## Analogie Ctrl+Z ⌨️

Tu rotates un cube de 45° → Matrice R
Tu veux l'annuler → Applique R⁻¹
Résultat : cube dans position originale !


## Condition d'existence
✅ A⁻¹ existe si det(A) ≠ 0
❌ A⁻¹ n'existe PAS si det(A) = 0 (matrice singulière)

## Applications majeures

### Résolution de systèmes 📊
# Résoudre Ax = b
# Solution : x = A⁻¹ × b
# (si A⁻¹ existe !)
Graphisme 3D 🎮

Annuler transformations : retour à l'état initial
Calculs de caméra : view matrix inverse
Animations : trajectoires inverses

Cryptographie 🔐

Chiffrement matriciel : A encode, A⁻¹ décode
Sécurité : si pas d'inverse → indéchiffrable !

Point technique
💰 Coût élevé : O(n³) - très lent pour grandes matrices
🔥 Instabilité numérique : attention si det ≈ 0
