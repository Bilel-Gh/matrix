from ex00.vector import Vector


def angle_cos(v: Vector, u: Vector) -> float:
    """
    Calculate the cosine of the angle between two vectors.

    Args:
        v (Vector): The first vector.
        u (Vector): The second vector.

    Returns:
        float: The cosine of the angle between the two vectors.

    Raises:
        ValueError: If the vectors do not have the same length or if one or
         both vectors are null.
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Arguments must be Vectors")
    if v.shape() != u.shape():
        raise ValueError("vectors must have same len")
    norm_product = u.norm() * v.norm()
    if norm_product == 0:
        raise ValueError("One or both vectors are null")
    result = u.dot(v) / norm_product

    if result > 0.99999999999:
        return 1.0
    if result < -0.99999999999:
        return -1.0
    return result


if __name__ == "__main__":
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(angle_cos(u, v))  # 1.0 (même direction)

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(angle_cos(u, v))  # 0.0 (perpendiculaire)

    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print(angle_cos(u, v))  # -1.0 (directions opposées)
