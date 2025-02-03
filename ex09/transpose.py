# test_transpose.py
from ex00.matrix import Matrix

if __name__ == "__main__":
    print("\n=== Test de la Transposition de Matrices ===\n")

    # Test 1: Matrice carrée 2x2
    print("Test 1: Matrice carrée 2x2")
    m1 = Matrix([[1., 2.],
                 [3., 4.]])
    print("Matrice originale:")
    print(m1)
    print("\nMatrice transposée:")
    print(m1.transpose())

    # Test 2: Matrice rectangulaire 2x3
    print("\nTest 2: Matrice rectangulaire 2x3")
    m2 = Matrix([[1., 2., 3.],
                 [4., 5., 6.]])
    print("Matrice originale:")
    print(m2)
    print("\nMatrice transposée:")
    print(m2.transpose())

    # Test 3: Matrice avec nombres négatifs
    print("\nTest 3: Matrice avec nombres négatifs")
    m3 = Matrix([[8., 5., -2.],
                 [4., 7., 20.]])
    print("Matrice originale:")
    print(m3)
    print("\nMatrice transposée:")
    print(m3.transpose())
