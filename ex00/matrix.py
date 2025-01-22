class Matrix:
    def __init__(self, data):
        """
        Initialize a matrix.
        Args:
            data (list[list[float]]): 2D list of numbers
        """
        if not data or not data[0]:
            raise ValueError("Matrice cannot be empty")

        self.rows = len(data)
        self.cols = len(data[0])

        self.values = [[float(x) for x in row] for row in data]

        if not all(len(row) == self.cols for row in self.values):
            raise ValueError("All rows must have same length")

    def __str__(self):
        """
        Return a string representation of the matrice.

        :return:
        str: A string representation with each row on a new line,
             elements separated by commas

        """
        return '\n'.join(f"[{', '.join(str(x) for x in row)}]" for row in self.values)

    def shape(self):
        """
        Return the dimensions of the matrice.
        Returns:
            tuple: (number of rows, number of columns)
        """
        return self.rows, self.cols

    def add(self, m):
        """
        add another matrix to this matrice (in-place).

        Args:
            m (matrice): The matrice that will be added

        Raises:
            ValueError: If matrices have different dimensions
        """
        if self.shape() != m.shape():
            raise ValueError("matrices must have same dimension")

        for r in range(self.rows):
            for c in range(self.cols):
                self.values[r][c] += m.values[r][c]

    def sub(self, m):
        """
        Subtract another matrice from this matrice (in-place).

        Args:
            m (matrice): The matrice to subtract

        Raises:
            ValueError: If matrices have different dimensions
        """
        if self.shape() != m.shape():
            raise ValueError("matrices must have same dimension")

        for r in range(self.rows):
            for c in range(self.cols):
                self.values[r][c] -= m.values[r][c]

    def scl(self, scalar):
        """
        Scale this matrice by a scalar (in-place).

        Args:
            scalar (float): The scalar to multiply by
        """
        for r in range(self.rows):
            for c in range(self.cols):
                self.values[r][c] *= scalar
