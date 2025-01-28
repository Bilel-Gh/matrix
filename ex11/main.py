from ex00.matrix import Matrix
import determinant

def print_test_case(matrix, expected_result=None):
    """
    Affiche un cas de test avec sa matrice et son résultat.
    Si expected_result est fourni, vérifie aussi si le résultat est correct.
    """
    print("Matrice de test :")
    print(matrix)
    result = matrix.determinant()
    print(f"Déterminant : {result}")
    if expected_result is not None:
        print(f"Résultat attendu : {expected_result}")
        print(f"Test {'réussi' if abs(result - expected_result) < 1e-10 else 'échoué'}")
    print()

def main():
    # Test 1: Matrice 2x2 identité avec facteur 2
    print("Test 1: Matrice 2x2")
    m1 = Matrix([
        [2., 0.],
        [0., 2.]
    ])
    print_test_case(m1, 4.0)  # det = 2 * 2 = 4

    # Test 2: Matrice 3x3 du sujet
    print("Test 2: Matrice 3x3")
    m2 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])
    print_test_case(m2, -174.0)

    # Test 3: Matrice 4x4 du sujet
    print("Test 3: Matrice 4x4")
    m3 = Matrix([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.]
    ])
    print_test_case(m3, 1032.0)

if __name__ == "__main__":
    main()