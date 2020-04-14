import numpy as np


# noinspection PyPep8Naming
def dissection(A):
    rows, columns = np.shape(A)
    A_copy = np.copy(A)

    p = [0] * (columns - 1)
    L = [[0] * columns for i in range(columns)]
    for row in range(0, columns - 1):
        if A_copy[row][row] == 0:
            for i in range(row + 1, columns):
                if A_copy[i][row] != 0:
                    tmp = np.copy(A_copy[i])
                    A_copy[i] = A_copy[row]
                    A_copy[row] = tmp

                    tmp = np.copy(L[i])
                    L[i] = L[row]
                    L[row] = tmp

                    p[row] = i + 1
                    break

        for i in range(row + 1, columns):
            c = -A_copy[i][row] / A_copy[row][row]
            A_copy[i] = A_copy[i] + c * A_copy[row]
            L[i][row] = -c

    return (A_copy + L), p


# noinspection PyPep8Naming
def forward(LU, x):
    rows, columns = np.shape(LU)

    L = [[0] * rows for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, rows):
            if i == j:
                L[i][j] = 1

    for row in range(1, rows):
        for column in range(0, columns - 1):
            if row > column:
                L[row][column] = LU[row][column]

    L_inv = np.linalg.inv(L)
    return np.dot(L_inv, x)


# noinspection PyPep8Naming
def backwards(LU, x):
    rows, columns = np.shape(LU)
    LU_copy = np.copy(LU)

    for row in range(1, rows):
        for column in range(0, columns - 1):
            if row > column:
                LU_copy[row][column] = 0

    U_inv = np.linalg.inv(LU_copy)
    return np.dot(U_inv, x)


def permutation(p, x):
    x_copy = np.copy(x)

    for i, pi in enumerate(p):
        h = x_copy[i]
        x_copy[i] = x_copy[pi - 1]
        x_copy[pi - 1] = h
    return x_copy


# noinspection PyPep8Naming,PyShadowingNames
def shermanMorrison(A_roof, u, v, b_roof):
    LU, p = dissection(A_roof)

    y = forward(LU, permutation(p, u))
    z = backwards(LU, y)

    if 1 + np.dot(v, z) == 0:
        return "Matrix nicht regulaer."

    alpha = 1. / (1 + np.dot(v, z))
    y_roof = forward(LU, permutation(p, b_roof))
    z_roof = backwards(LU, y_roof)
    return z_roof - np.dot(alpha, np.dot(np.dot(v, z_roof), z))


A_roof = np.copy([[0, 0, 0, 1], [2, 1, 2, 1], [4, 4, 0, 2], [2, 3, 1, 3]])
u = [0, 1, 2, 3]
v = [0, 0, 0, 1]
b_roof = [3, 5, 4, 5]

print(shermanMorrison(A_roof, u, v, b_roof))
