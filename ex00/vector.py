class Vector:
    def __init__(self, data):
        """
        Initialize a Vector instance.

        Parameters:
        data : A list of integers or floats to initialize the vector.

        Attributes:
        values : A list of floats representing the vector's values.
        """
        self.values = [float(x) for x in data]

    def __str__(self):
        """
        Return a string representation of the vector.

        Returns:
        str: A string where each element of the vector is enclosed in square brackets and separated by newlines.
        """
        return '\n'.join(f"[{x}]" for x in self.values)

    def shape(self):
        """
        return the shape of a vector.
        """
        return len(self.values)

    def add(self, v):
        """
        add another vector to this vector (in-place).

        Args:
            v (Vector): The vector that will be added

        Raises:
            ValueError: If vectors have different dimensions
        """
        if self.shape() != v.shape():
            raise ValueError("Vectors must have same dimension")

        for i in range(self.shape()):
            self.values[i] += v.values[i]

    def sub(self, v):
        """
        Subtract another vector from this vector (in-place).

        Args:
            v (Vector): The vector to subtract

        Raises:
            ValueError: If vectors have different dimensions
        """
        if self.shape() != v.shape():
            raise ValueError("Vectors must have same dimension")

        for i in range(self.shape()):
            self.values[i] -= v.values[i]

    def scl(self, scalar):
        """
        Scale this vector by a scalar (in-place).

        Args:
            scalar (float): The scalar to multiply by
        """
        for i in range(self.shape()):
            self.values[i] *= scalar