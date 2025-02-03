from ex12.inverse import MatrixWithInverse as Matrix


def main():
    """
    Programme de test pour la fonction inverse() suivant les exemples du sujet.
    Teste différents cas de matrices et vérifie les résultats attendus.
    """
    print("=== Test de l'inversion de matrices ===\n")

    # Test 1: Matrice identité 3x3
    print("Test 1: Matrice identité")
    print("La matrice identité devrait être égale à son inverse")
    m1 = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])
    print("Matrice originale:")
    print(m1)
    print("Son inverse:")
    print(m1.inverse())
    print()

    # Test 2: Matrice diagonale simple
    print("Test 2: Matrice diagonale")
    print("Une matrice diagonale [2] doit avoir pour inverse [1/2]")
    m2 = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.]
    ])
    print("Matrice originale:")
    print(m2)
    print("Son inverse:")
    print(m2.inverse())
    print()

    # Test 3: Matrice complexe 3x3
    print("Test 3: Matrice complexe 3x3")
    m3 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])
    print("Matrice originale:")
    print(m3)
    print("Son inverse:")
    print(m3.inverse())
    print()

    # Test 4: Matrice non inversible (déterminant nul)
    print("Test 4: Matrice non inversible")
    print("Cette matrice doit lever une exception car son déterminant est nul")
    try:
        m4 = Matrix([
            [1., 2.],
            [2., 4.]
        ])
        print("Matrice originale:")
        print(m4)
        print("Tentative d'inversion:")
        print(m4.inverse())
    except ValueError as e:
        print(f"Exception levée comme prévu: {e}")
    print()

    # Test 5: Vérification de A * A^(-1) = I
    print("Test 5: Vérification de A * A^(-1) = I")
    print(
        "Le produit d'une matrice par son inverse doit"
        " donner la matrice identité")
    m5 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])
    m5_inv = m5.inverse()
    print("\nVérification de A * A^(-1):")
    print("Matrice originale * son inverse:")
    print(m5.mul_mat(m5_inv))  # Devrait donner la matrice identité
    print()


if __name__ == "__main__":
    main()
