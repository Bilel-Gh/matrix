from .vector import Vector
from .matrix import Matrix

def matrix_to_vector(matrix: Matrix) -> Vector:
    """Convert a matrix to a vector by flattening."""
    vector_data = []
    for row in matrix.values:
        vector_data.extend(row)
    return Vector(vector_data)


def vector_to_matrix(vector: Vector, rows: int, cols: int) -> Matrix:
    """Convert a vector to a matrix with specified shape."""
    if rows * cols != vector.shape():
        raise ValueError("Invalid dimensions for reshaping")

    matrix_data = []
    for i in range(rows):
        row = vector.values[i * cols: (i + 1) * cols]
        matrix_data.append(row)

    return Matrix(matrix_data)