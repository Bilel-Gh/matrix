## Concept
Mesure la "ressemblance" entre deux directions, indépendamment de leur taille.

C'est comme mesurer l'angle entre deux flèches, mais d'une façon spéciale qui donne 1 si elles pointent dans la même direction, 0 si elles sont perpendiculaires, et -1 si elles pointent dans des directions opposées.

## Formule
cos(angle) = (u • v) / (||u|| × ||v||)

## Interprétation
+1.0 → directions identiques (0°) ➡️➡️
0.0 → perpendiculaires (90°) ➡️⬆️
-1.0 → directions opposées (180°) ➡️⬅️

## Exemple Netflix 📺
# Goûts utilisateur A : [Action=5, Romance=1, Horreur=0]
# Goûts utilisateur B : [Action=3, Romance=2, Horreur=0]
#
# cos = 0.8 → goûts similaires → recommande les mêmes films !
Applications

Recommandations : utilisateurs similaires
Reconnaissance faciale : comparaison de visages
Recherche : similarité de documents
Jeux : IA qui détecte le joueur dans son champ de vision

Point technique
🎯 Normalisation automatique : ignore la "force" des vecteurs, ne garde que la direction !
