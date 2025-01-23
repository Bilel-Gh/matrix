from ex00.matrix import Matrix
from ex00.vector import Vector


class Matrice:
    pass


if __name__ == "__main__":
    # Test 1: produit vectoriel entre vecteur vertical et horizontal
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
    v = Vector([5, 6])

    # result = m1.mul_vec(v)
    # print("result = ", result)
    print(m1)
    print("---")
    print(m2)
    result2 = m1.mul_mat(m2)