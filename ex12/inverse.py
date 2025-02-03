from ex11.determinant import MatrixWithDeterminant as Matrix


class MatrixWithInverse(Matrix):
    def inverse(self) -> 'Matrix':
        """
        Calcule l'inverse de la matrice en utilisant la méthode
         de Gauss-Jordan.
        La méthode fonctionne en créant une matrice augmentée [A|I]
         puis en la réduisant
        pour obtenir [I|A^(-1)].
        """
        # Vérifie si la matrice est carrée
        if len(self.values) != len(self.values[0]):
            raise ValueError(
                "La matrice doit être carrée pour être inversible")

        # Vérifie si la matrice est inversible avec le déterminant
        if abs(self.determinant()) < 1e-10:
            raise ValueError(
                "La matrice n'est pas inversible (déterminant nul)")

        n = len(self.values)

        # Crée la matrice augmentée [A|I]
        augmented_values = []
        for i in range(n):
            row = []
            # Partie matrice originale
            for j in range(n):
                row.append(self.values[i][j])
            # Partie identité
            for j in range(n):
                row.append(1.0 if i == j else 0.0)
            augmented_values.append(row)

        # Crée la matrice augmentée et la réduit
        augmented = Matrix(augmented_values)
        reduced = augmented.row_echelon()

        # Extrait la partie droite qui contient l'inverse
        result = Matrix([[0.0] * n for _ in range(n)])
        for i in range(n):
            for j in range(n):
                result.values[i][j] = reduced.values[i][j + n]

        return result
