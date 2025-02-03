from ex12.inverse import MatrixWithInverse as Matrix


class MatrixFinal(Matrix):
    def rank(self) -> int:
        """
        Calcule le rang de la matrice.
        Le rang est le nombre de lignes non nulles dans la forme échelonnée.
        """
        echelon_form = self.row_echelon()

        rank = 0
        for i in range(echelon_form.rows):
            is_nonzero = False
            for j in range(echelon_form.cols):
                if abs(echelon_form.values[i][j]) > 1e-10:
                    is_nonzero = True
                    break
            if is_nonzero:
                rank += 1

        return rank
