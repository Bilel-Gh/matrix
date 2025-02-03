from ex10.row_echelon import MatrixWithRowEchelon as Matrix


def main():
    """
    Programme de test pour la méthode row_echelon() basé sur les exemples du
     sujet. Chaque test affiche la matrice d'entrée et sa forme échelonnée
     résultante.
    """
    print("=== Test 1: Matrice identité 3x3 ===")
    print("Cette matrice devrait rester inchangée car elle est déjà sous forme"
          " échelonnée")
    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])
    print("\nMatrice originale:")
    print(m1)
    print("\nForme échelonnée:")
    print(m1.row_echelon())
    print("\n" + "=" * 50)

    print("\n=== Test 2: Matrice 2x2 simple ===")
    print("Cette matrice devrait se réduire à une forme échelonnée avec des 1"
          " sur la diagonale")
    m2 = Matrix([
        [1.0, 2.0],
        [3.0, 4.0]
    ])
    print("\nMatrice originale:")
    print(m2)
    print("\nForme échelonnée:")
    print(m2.row_echelon())
    print("\n" + "=" * 50)

    print("\n=== Test 3: Matrice 2x2 avec ligne dépendante ===")
    print("Cette matrice devrait avoir une ligne de zéros car les lignes sont"
          " linéairement dépendantes")
    m3 = Matrix([
        [1.0, 2.0],
        [2.0, 4.0]
    ])
    print("\nMatrice originale:")
    print(m3)
    print("\nForme échelonnée:")
    print(m3.row_echelon())
    print("\n" + "=" * 50)

    print("\n=== Test 4: Matrice 3x5 complexe ===")
    print("Cette matrice teste la manipulation de nombres plus complexes")
    m4 = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0]
    ])
    print("\nMatrice originale:")
    print(m4)
    print("\nForme échelonnée:")
    print(m4.row_echelon())
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
