from ex00.matrix import Matrix


class MatrixWithRowEchelon(Matrix):
    def is_pivot_in_row(self, row: list, start_col: int = 0) -> bool:
        """
        Vérifie si un pivot existe dans la rangée à partir
         d'une colonne donnée. Un pivot est considéré comme existant si sa
         valeur absolue est supérieure
         à 1e-10.
        """
        for i in range(start_col, len(row)):
            if abs(row[i]) > 1e-10:
                return True
        return False

    def get_pivot_col(self, row: list, start_col: int = 0) -> int:
        """
        Retourne l'index du premier pivot non-nul dans la rangée.
        Renvoie -1 si aucun pivot n'est trouvé.
        """
        for i in range(start_col, len(row)):
            if abs(row[i]) > 1e-10:
                return i
        return -1

    def find_best_pivot_row(self, curr_col: int, start_row: int) -> int:
        """
        Trouve la meilleure ligne pour le pivot dans une colonne donnée.
        Retourne l'index de la ligne avec la plus grande valeur absolue.
        """
        best_row = start_row
        max_value = abs(self.values[start_row][curr_col])

        for row in range(start_row + 1, self.rows):
            curr_value = abs(self.values[row][curr_col])
            if curr_value > max_value:
                max_value = curr_value
                best_row = row

        return best_row if max_value > 1e-10 else -1

    def sub_row(self, first_row: list, curr_row: list, factor: float):
        """
        Soustrait une rangée multipliée par un facteur d'une autre rangée.
        first_row - factor * curr_row
        """
        for i in range(len(curr_row)):
            curr_row[i] = curr_row[i] - factor * first_row[i]

    def div_row(self, row: list, dividor: float):
        """
        Divise une rangée par un scalaire non-nul.
        Vérifie d'abord si le diviseur n'est pas trop proche de zéro.
        """
        if abs(dividor) < 1e-10:
            return
        for i in range(len(row)):
            row[i] = row[i] / dividor

    def swap_rows(self, row1: int, row2: int):
        """
        Échange deux lignes de la matrice
        """
        self.values[row1], self.values[row2] = self.values[row2], self.values[
            row1]

    def row_echelon(self) -> 'Matrix':
        """
        Calcule la forme échelonnée de la matrice.
        Retourne une nouvelle matrice en forme échelonnée.
        """
        result = MatrixWithRowEchelon(
            [[self.values[i][j] for j in range(self.cols)]
             for i in range(self.rows)])

        curr_row = 0
        curr_col = 0

        while curr_row < result.rows and curr_col < result.cols:
            best_row = result.find_best_pivot_row(curr_col, curr_row)

            # Si aucun pivot valide n'est trouvé, passe à la colonne suivante
            if best_row == -1:
                curr_col += 1
                continue

            # Si nécessaire, échange les lignes pour avoir le meilleur pivot
            if best_row != curr_row:
                result.swap_rows(curr_row, best_row)

            # Normalise la ligne du pivot (divise par le pivot pour avoir un 1)
            pivot = result.values[curr_row][curr_col]
            result.div_row(result.values[curr_row], pivot)

            # Élimine le pivot des lignes suivantes
            for row in range(result.rows):
                if row != curr_row and abs(
                        result.values[row][curr_col]) > 1e-10:
                    factor = result.values[row][curr_col]
                    result.sub_row(
                        result.values[curr_row],
                        result.values[row],
                        factor)

            curr_row += 1
            curr_col += 1

        return result
