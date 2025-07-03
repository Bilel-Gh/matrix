## Concept
Calculer des points intermédiaires entre deux valeurs.

Imagine que tu marches de ta maison à l'école. L'interpolation te dit où tu te trouves sur le chemin. Si t=0, tu es à la maison, si t=1, tu es à l'école, et si t=0.5, tu es à mi-chemin !

## Principe
lerp(A, B, t) où t ∈ [0, 1]

t = 0   → résultat = A (début)
t = 0.5 → résultat = milieu de A et B
t = 1   → résultat = B (fin)


## Exemple concret
# Animation d'un personnage
position_start = [0, 0]    # Début du level
position_end = [100, 50]   # Fin du level

# À 30% du parcours :
current_pos = lerp(start, end, 0.3)  # [30, 15]
Applications

Netflix : animations des menus
Jeux vidéo : déplacement fluide des objets
Apps mobiles : transitions entre écrans
CSS : animations web

Point technique
✨ Fonctionne avec tout : nombres, vecteurs, matrices, couleurs !
