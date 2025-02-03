from ex00.matrix import Matrix
from ex00.vector import Vector


def lerp(u, v, t: float):
    """
    Linear Interpolation Function (lerp)

    Calcule un point entre deux valeurs u et v selon un facteur t.
    La formule est : lerp(u, v, t) = u + t * (v - u)

    Exemples :
    - u = point de départ, v = point d'arrivée
    - t = 0: résultat = u (point de départ)
    - t = 0.5: résultat = point à mi-chemin
    - t = 1: résultat = v (point d'arrivée)

    Fonctionne avec :
    - nombres (int/float)
    - vecteurs (additionne élément par élément)
    - matrices (additionne élément par élément)

    Crée une copie pour éviter de modifier les valeurs d'origine.
    """

    if not isinstance(t, (int, float)) and not isinstance(t, bool):
        raise TypeError("t must be numeric (int or float)")
    if not isinstance(u, (int, float, Vector, Matrix)):
        raise TypeError("u must be a number, Vector, or Matrix")
    if not isinstance(v, type(u)):
        raise TypeError("u and v must be same type")

    if isinstance(u, (int, float)):
        return u + t * (v - u)

    if isinstance(u, (Vector, Matrix)):
        if not isinstance(v, type(u)):
            raise ValueError("u and v must be same type")
        # copy u
        result = type(u)(u.values[:] if isinstance(u, Vector)
                         else [row[:] for row in u.values])

        if isinstance(u, Vector):
            for i in range(len(result.values)):
                result.values[i] = lerp(u.values[i], v.values[i], t)
        else:  # if matrix
            for i in range(len(result.values)):
                for j in range(len(result.values[0])):
                    result.values[i][j] = lerp(u.values[i][j], v.values[i][j],
                                               t)

        return result


if __name__ == "__main__":
    # Test avec des nombres
    print(lerp(0., 1., 0.))  # 0.0
    print(lerp(0., 1., 1.))  # 1.0
    print(lerp(0., 1., 0.5))  # 0.5

    # Test avec des vecteurs
    v1 = Vector([2., 1.])
    v2 = Vector([4., 2.])
    print(lerp(v1, v2, 0.3))  # [2.6, 1.3]

    # Test avec des matrices
    m1 = Matrix([[2., 1.], [3., 4.]])
    m2 = Matrix([[20., 10.], [30., 40.]])
    print(lerp(m1, m2, 0.5))  # [[11.0, 5.5], [16.5, 22.0]]
