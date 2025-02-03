from ex00.vector import Vector

if __name__ == "__main__":
    # Test avec les exemples du sujet
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))  # Affiche: 0.0 (vecteurs perpendiculaires)

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))  # Affiche: 2.0 (vecteurs parallèles)

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))  # Affiche: 9.0
