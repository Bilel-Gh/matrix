from ex00.vector import Vector

if __name__ == "__main__":
    # Test 1: produit vectoriel entre vecteur vertical et horizontal
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    result = u.cross_product(v)
    print(result)  # Devrait afficher: [0.0] [1.0] [0.0]

    # Test 2: exemple plus complexe
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    result = u.cross_product(v)
    print(result)  # Devrait afficher: [-3.0] [6.0] [-3.0]