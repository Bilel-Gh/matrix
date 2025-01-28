from ex00.matrix import Matrix

def det_2x2(self, matrix) -> float:
    """
    Calcule le déterminant d'une matrice 2x2.
    Formule: ad - bc pour une matrice [[a,b],[c,d]]
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det_3x3(self, matrix) -> float:
    """
    Calcule le déterminant d'une matrice 3x3 en utilisant la règle de Sarrus.
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    # Les termes positifs
    term1 = a * e * i
    term2 = b * f * g
    term3 = c * d * h

    # Les termes négatifs
    term4 = c * e * g
    term5 = a * f * h
    term6 = b * d * i

    return term1 + term2 + term3 - term4 - term5 - term6


def get_submatrix(self, matrix, skip_row: int, skip_col: int) -> list:
    """
    Crée une sous-matrice en excluant une ligne et une colonne spécifiées.
    Utilisé pour le calcul du déterminant par développement de Laplace.
    """
    submatrix = []
    for i in range(len(matrix)):
        if i != skip_row:  # On saute la ligne à ignorer
            row = []
            for j in range(len(matrix)):
                if j != skip_col:  # On saute la colonne à ignorer
                    row.append(matrix[i][j])
            submatrix.append(row)
    return submatrix


def det_4x4(self, matrix) -> float:
    """
    Calcule le déterminant d'une matrice 4x4 par développement de Laplace
    selon la première ligne.
    """
    result = 0
    for j in range(4):
        # 1. Obtenir le coefficient sur la première ligne
        coef = matrix[0][j]
        # 2. Obtenir la sous-matrice 3x3 correspondante
        submatrix = self.get_submatrix(matrix, 0, j)
        # 3. Calculer le signe : alterne entre +1 et -1
        sign = (-1) ** j
        # 4. Calculer et ajouter le terme au résultat
        term = coef * sign * self.det_3x3(submatrix)
        result += term

    return result


def determinant(self) -> float:
    """
    Calcule le déterminant de la matrice.
    Ne fonctionne que pour les matrices carrées jusqu'à 4x4.
    """
    # Vérifie si la matrice est carrée
    if len(self.values) != len(self.values[0]):
        raise ValueError("La matrice doit être carrée")

    size = len(self.values)

    # Gestion selon la taille de la matrice
    if size == 1:
        return self.values[0][0]
    elif size == 2:
        return self.det_2x2(self.values)
    elif size == 3:
        return self.det_3x3(self.values)
    elif size == 4:
        return self.det_4x4(self.values)
    else:
        raise ValueError("Cette implémentation ne gère que les matrices jusqu'à 4x4")

Matrix.determinant = determinant
Matrix.det_2x2 = det_2x2
Matrix.det_3x3 =det_3x3
Matrix.det_4x4 =det_4x4
Matrix.get_submatrix = get_submatrix