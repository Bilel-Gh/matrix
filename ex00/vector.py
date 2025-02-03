class Vector:
    def __init__(self, data):
        """
        Initialize a Vector instance.

        Parameters:
        data : A list of integers or floats to initialize the vector.

        Attributes:
        values : A list of floats representing the vector's values.
        """
        for value in data:
            if not isinstance(data, list):
                raise TypeError("Input must be a list")

            if not data:
                raise ValueError("Vector cannot be empty")

            if not all(self.is_numeric(x) for x in data):
                raise TypeError("All elements must be numeric (int or float)")

        self.values = [float(x) for x in data]

    def is_numeric(self, value):
        """
        Vérifie si une valeur est numérique (int ou float)
        """
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def format_number(self, x):
        """
        Format a number with special handling for very small values close to
         zero.
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
        Return a string representation of the vector.

        Returns:
        str: A string where each element of the vector is enclosed in square
         brackets and separated by newlines.
        """
        return "\n".join(f"[{self.format_number(x)}]" for x in self.values)

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

    def dot(self, v: "Vector") -> float:
        """
        Calcule le produit scalaire entre deux vecteurs (dot product).

        Le produit scalaire est la somme des produits des composantes :
        [a1, a2] · [b1, b2] = (a1 * b1) + (a2 * b2)

        Args:
            v: Second vecteur pour le produit scalaire

        Returns:
            float: Résultat du produit scalaire

        Raises:
            ValueError: Si les vecteurs n'ont pas la même dimension
        """
        if self.shape() != v.shape():
            raise ValueError("Vectors must have same dimension")
        result = 0
        for a, b in zip(self.values, v.values):
            result += a * b

        return result

    def norm_1(self) -> float:
        """
        Calcule la norme-1 (Manhattan) du vecteur.

        La norme-1 est la somme des valeurs absolues des composantes :
        Pour un vecteur [x₁, x₂, ..., xₙ], norme = |x₁| + |x₂| + ... + |xₙ|

        Returns:
            float: La norme-1 du vecteur

        Example:
            v = Vector([1, -2, 3])
            v.norm_1()  # Retourne 6 (|1| + |-2| + |3| = 1 + 2 + 3 = 6)
        """
        result = 0
        for x in self.values:
            if x > 0:
                value = x
            else:
                value = -x
            result += value
        return result

    def norm(self) -> float:
        """
        Calcule la norme-2 (Euclidienne) du vecteur.

        La norme-2 est la racine carrée de la somme des carrés des
        composantes :
        Pour un vecteur [x₁, x₂, ..., xₙ], norme = √(x₁² + x₂² + ... + xₙ²)

        Returns:
            float: La norme-2 (Euclidienne) du vecteur

        Example:
            v = Vector([3, 4])
            v.norm()  # Retourne 5.0 (√(3² + 4²) = √(9 + 16) = √25 = 5)
        """
        sum_squares = 0
        for x in self.values:
            sum_squares += x * x  # ou pow(x, 2)
        return pow(sum_squares, 0.5)  # pow(x, 0.5) = racine carre de x

    def norm_inf(self) -> float:
        """
        Calcule la norme infinie (maximum) du vecteur.

        La norme infinie est la plus grande valeur absolue parmi les
        composantes :
        Pour un vecteur [x₁, x₂, ..., xₙ], norme = max(|x₁|, |x₂|, ..., |xₙ|)

        Returns:
            float: La norme infinie du vecteur

        Example:
            v = Vector([1, -5, 3])
            v.norm_inf()  # Retourne 5 (max(|1|, |-5|, |3|) = max(1, 5, 3) = 5)
        """
        result = 0
        for x in self.values:
            if x > 0:
                value = x
            else:
                value = -x
            result = max(result, value)
        return result

    def cross_product(self, v: "Vector") -> "Vector":
        """
        Calcule le produit vectoriel avec un autre vecteur 3D.
        Le produit vectoriel donne un vecteur perpendiculaire aux deux
        vecteurs d'entrée.

        Args:
            v: Second vecteur 3D

        Returns:
            Vector: Le vecteur résultant du produit vectoriel

        Raises:
            ValueError: Si les vecteurs ne sont pas de dimension 3
        """
        # Vérification du type
        if not isinstance(v, Vector):
            raise TypeError("Argument must be a Vector")

        if self.shape() != 3 or v.shape() != 3:
            raise ValueError("Cross product only works with 3D vectors")

        x1, y1, z1 = self.values[0], self.values[1], self.values[2]
        x2, y2, z2 = v.values[0], v.values[1], v.values[2]

        new_x = y1 * z2 - z1 * y2
        new_y = z1 * x2 - x1 * z2
        new_z = x1 * y2 - y1 * x2

        return Vector([new_x, new_y, new_z])
