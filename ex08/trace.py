# test_trace.py
from ex00.matrix import Matrix

if __name__ == "__main__":
    print("\n=== Test de la Trace de Matrices ===\n")

    # Test 1: Matrice identité 2x2
    print("Test 1: Matrice identité 2x2")
    m1 = Matrix([[1., 0.],
                 [0., 1.]])
    print("Matrice:")
    print(m1)
    print(f"Trace: {m1.trace()}")  # Devrait afficher 2.0

    # Test 2: Matrice 3x3 avec nombres variés
    print("\nTest 2: Matrice 3x3")
    m2 = Matrix([[2., -5., 0.],
                 [4., 3., 7.],
                 [-2., 3., 4.]])
    print("Matrice:")
    print(m2)
    print(f"Trace: {m2.trace()}")  # Devrait afficher 9.0

    # Test 3: Matrice 3x3 avec diagonale simple
    print("\nTest 3: Matrice avec diagonale facile à calculer")
    m3 = Matrix([[1., 0., 0.],
                 [0., 2., 0.],
                 [0., 0., 3.]])
    print("Matrice:")
    print(m3)
    print(f"Trace: {m3.trace()}")  # Devrait afficher 6.0
