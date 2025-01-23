from ex00.vector import Vector

def angle_cos(v: Vector, u: Vector) -> float:
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