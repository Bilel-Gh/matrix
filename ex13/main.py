from ex13.rank import MatrixFinal as Matrix


def main():
    # Test 1: Matrice identité 3x3 (rang plein = 3)
    m1 = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    print("Rang de la matrice identité:", m1.rank())  # Devrait afficher 3

    # Test 2: Matrice avec une ligne dépendante
    m2 = Matrix([
        [1, 2, 0],
        [2, 4, 0],  # Cette ligne est le double de la première
        [0, 0, 1]
    ])
    print("Rang de la matrice avec ligne dépendante:",
          m2.rank())  # Devrait afficher 2

    # Test 3: Matrice du sujet
    m3 = Matrix([
        [8, 5, -2],
        [4, 7, 20],
        [7, 6, 1],
        [21, 18, 7]
    ])
    print("Rang de la matrice du sujet:", m3.rank())  # Devrait afficher 3


if __name__ == "__main__":
    main()
