from ex00.vector import Vector

def linear_combination(vectors: list[Vector], coefs: list[float]) -> Vector:
    """
    Linear Combination Function

    La combinaison linéaire est une opération mathématique fondamentale qui combine
    plusieurs vecteurs en les multipliant chacun par un coefficient et en les additionnant
    Pour des vecteurs v₁, v₂, ..., vₙ et des coefficients c₁, c₂, ..., cₙ
    Résultat = (c₁*v₁) + (c₂*v₂) + ... + cₙvₙ

    Exemple avec 2 vecteurs :
    vectors = [v1, v2], coefs = [a, b]
    Résultat = a*v1 + b*v2

    Le processus :
    1. Vérifie que les dimensions correspondent
    2. Crée un vecteur de zéros de même dimension
    3. Pour chaque (vecteur, coefficient):
      - Multiplie le vecteur par son coefficient
      - Ajoute le résultat au vecteur final

    Les vecteurs doivent :
    - Être de même dimension
    - Avoir autant de coefficients que de vecteurs
    """
    if len(vectors) != len(coefs):
        raise ValueError("list of vectors and coefs must have same len")
    if not vectors:
        raise ValueError("Lists cannot be empty")
    dim = vectors[0].shape()
    if not all(v.shape() == dim for v in vectors):
        raise ValueError("All vectors must have same dimension")

    v_result = Vector([0.0] * dim) # init vector with 0 values

    for vec, coef in zip(vectors, coefs):
        temp = Vector(vec.values[:])
        temp.scl(coef)
        v_result.add(temp)

    return v_result


if __name__ == "__main__":
    # Test avec les exemples du sujet
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    result = linear_combination([e1, e2, e3], [10., -2., 0.5])
    print(result)
    # [10.0]
    # [-2.0]
    # [0.5]

