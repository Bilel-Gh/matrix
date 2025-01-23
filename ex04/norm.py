from ex00.vector import Vector

if __name__ == "__main__":
    print("\n=== Test des normes ===")

    # Test avec vecteur nul
    print("\nTest 1: Vecteur nul")
    u = Vector([0., 0., 0.])
    print(f"Vector: \n{u}")
    print(f"Norme 1: {u.norm_1()}")
    # note : python contrairement a rust affiche par défaut toute la précision disponible du float
    # python privilegie la précision maximale par défaut plutot que la lisibilite
    # 3.7416573867739413 plutot que 3.74165738
    print(f"Norme 2: {u.norm()}")
    print(f"Norme inf: {u.norm_inf()}")
    # Devrait afficher: 0.0, 0.0, 0.0

    # Test avec vecteur positif
    print("\nTest 2: Vecteur positif")
    u = Vector([1., 2., 3.])
    print(f"Vector: \n{u}")
    print(f"Norme 1: {u.norm_1()}")
    print(f"Norme 2: {u.norm()}")
    print(f"Norme inf: {u.norm_inf()}")
    # Devrait afficher: 6.0, 3.74165738, 3.0

    # Test avec vecteur négatif
    print("\nTest 3: Vecteur avec négatifs")
    u = Vector([-1., -2.])
    print(f"Vector: \n{u}")
    print(f"Norme 1: {u.norm_1()}")
    print(f"Norme 2: {u.norm()}")
    print(f"Norme inf: {u.norm_inf()}")
    # Devrait afficher: 3.0, 2.236067977, 2.0
