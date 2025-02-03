from ex00.vector import Vector


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

        for row in data:
            for value in row:
                if not isinstance(value, (float, int)):
                    raise ValueError("all values must be numbers")

        self.values = [[float(x) for x in row] for row in data]

        if not all(len(row) == self.cols for row in self.values):
            raise ValueError("All rows must have same length")

    def is_numeric(self, value):
        """
        Vérifie si une valeur est numérique (int ou float)
        """
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def format_number(self, x):
        """
        Format a number with special handling for very small
         values close to zero.
        Args:
            x (float): The number to format.
        Returns:
            str: The formatted number as a string.
        """
        if abs(x) < 1e-10:
            return "0.0"
        formatted = f"{x:.7f}".rstrip("0").rstrip(".")
        if "." not in formatted:
            formatted += ".0"
        return formatted

    def __str__(self):
        """
        Return a string representation of the matrice.

        :return:
        str: A string representation with each row on a new line,
             elements separated by commas

        """
        return "\n".join(
            f"[{', '.join(str(self.format_number(x)) for x in row)}]"
            for row in self.values
        )

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

    def mul_vec(self, vec: Vector) -> Vector:
        """
        Multiplie la matrice par un vecteur.
        Pour chaque ligne de la matrice, fait un produit
         scalaire avec le vecteur.

        Args:
            vec: Vecteur à multiplier (doit avoir même dimension
             que nombre de colonnes)
        Returns:
            Vector: Résultat de la multiplication
        """
        if self.cols != vec.shape():
            raise ValueError("Matrix columns must match vector size")

        result = []

        for r in range(self.rows):
            sum_product_row = 0
            for c in range(self.cols):
                sum_product_row += self.values[r][c] * vec.values[c]
            result.append(sum_product_row)
        return Vector(result)

    def mul_mat(self, mat: "Matrix") -> "Matrix":
        """
        Multiplie cette matrice par une autre matrice.
        Pour chaque position (i,j) dans la matrice résultat :
        - Prend la ligne i de la première matrice
        - Prend la colonne j de la deuxième matrice
        - Fait leur produit scalaire
        """
        if self.cols != mat.rows:
            raise ValueError(
                "First matrix columns must match second matrix rows")

        # _ car on ne se sert pas de la variable d'itération
        result = [[0 for _ in range(mat.cols)] for _ in range(self.rows)]

        # La boucle i sélectionne quelle ligne de la matrice A(self) on utilise
        for i in range(self.rows):
            # La boucle j sélectionne quelle colonne de la matrice B(mat) on
            # utilise
            for j in range(mat.cols):
                sum_product = 0
                # La boucle k nous fait avancer en même temps sur :
                # - la ligne i de A (de gauche à droite)
                # - la colonne j de B (de haut en bas)
                for k in range(
                        self.cols):  # self.cols car self.cols == mat.rows
                    sum_product += self.values[i][k] * mat.values[k][j]
                result[i][j] = sum_product

        return Matrix(result)

    def trace(self) -> float:
        """
        Calcule la trace de la matrice (somme de la diagonale principale).

        Returns:
            float: La somme des éléments diagonaux

        Raises:
            ValueError: Si la matrice n'est pas carrée
        """
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")

        result = 0
        for i in range(self.rows):
            result += self.values[i][i]

        return result

    def transpose(self) -> "Matrix":
        """
        Crée une nouvelle matrice qui est la transposée de celle-ci.
        Les lignes deviennent les colonnes et vice-versa.
        """
        # Crée une nouvelle matrice avec dimensions inversées
        # Si l'originale est 2x3(2rowx3col), la nouvelle sera 3x2(3rowx2col)
        result = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self.values[i][j]

        return Matrix(result)
