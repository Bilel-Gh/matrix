from ex00.matrix import Matrix
from ex00.vector import Vector


def print_separator():
    print("\n" + "=" * 50 + "\n")


def test_vector_operations():
    try:
        print("TEST VECTOR OPERATIONS")
        print("-" * 20)

        # Création des vecteurs
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])

        print("Vector u:")
        print(u)
        print("\nVector v:")
        print(v)

        # Test addition
        u_add = Vector([2.0, 3.0])
        u_add.add(v)
        print("\nResult of u + v:")
        print(u_add)

        # Test soustraction
        u_sub = Vector([2.0, 3.0])
        u_sub.sub(v)
        print("\nResult of u - v:")
        print(u_sub)

        # Test multiplication scalaire
        u_scl = Vector([2.0, 3.0])
        u_scl.scl(2.0)
        print("\nResult of u * 2:")
        print(u_scl)
    except Exception as e:
        print(f"Error: {str(e)}")


def test_matrix_operations():
    try:
        print("TEST MATRIX OPERATIONS")
        print("-" * 20)

        # Création des matrices
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])

        print("Matrix u:")
        print(u)
        print("\nMatrix v:")
        print(v)

        # Test addition
        u_add = Matrix([[1.0, 2.0], [3.0, 4.0]])
        u_add.add(v)
        print("\nResult of u + v:")
        print(u_add)

        # Test soustraction
        u_sub = Matrix([[1.0, 2.0], [3.0, 4.0]])
        u_sub.sub(v)
        print("\nResult of u - v:")
        print(u_sub)
    except Exception as e:
        print(f"Error: {str(e)}")

    # Test multiplication scalaire
    u_scl = Matrix([[1.0, 2.0], [3.0, 4.0]])
    u_scl.scl(2.0)
    print("\nResult of u * 2:")
    print(u_scl)


if __name__ == "__main__":
    print("\nTESTING MATRIX LIBRARY - EXERCISE 00\n")

    test_vector_operations()
    print_separator()

    test_matrix_operations()
    print_separator()

    print("All tests completed!")
