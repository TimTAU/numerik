import numpy as np


# Siehe Ha 2 Aufgabe 2
def permutation(p, x):
    for i in range(len(x)):
        tmp = x[i]
        x[i] = x[p[i] - 1]
        x[p[i] - 1] = tmp
    return x


# Siehe Ha 2 Aufgabe 2
# noinspection DuplicatedCode,PyPep8Naming
def vorwaerts(LU, x):
    for i in range(1, len(x)):
        add = 0
        for y in range(0, i):
            add += LU[i][y] * x[y]
        x[i] = x[i] - add

    return x


# Siehe Ha 2 Aufgabe 2
# noinspection PyPep8Naming
def rueckwaerts(LU, x):
    for i in range(len(x) - 1, -1, -1):
        add = 0
        for y in range(len(x) - 1, i, -1):
            add += LU[i][y] * x[y]
        x[i] = (x[i] - add) / LU[i][i]

    return x


# noinspection PyUnusedLocal
def pivot(A):
    n = len(A)

    L = [[0.] * n for i in range(n)]
    U = [[0.] * n for i in range(n)]
    P = [0. for i in range(n)]

    for elementI in range(0, n):
        for elementJ in range(0, n):
            U[elementI][elementJ] = A[elementI][elementJ]
            L[elementI][elementJ] = 0.

    for elementI in range(0, n):
        # Wenn das erste Diagonalelement 0 ist, wird die Zeile mit der nächsten mit ungleich 0 getauscht
        maxi = U[elementI][elementI]
        column = elementI + 1

        for elementK in range(column, n):
            if U[elementK][elementI] > maxi:
                maxi = U[elementK][elementI]
                column = elementK

        if maxi == U[elementI][elementI]:
            P[elementI] = elementI + 1
        else:  # Größeres Element gefunden
            tmp = U[column]
            tmp2 = L[column]
            U[column] = U[elementI]
            L[column] = L[elementI]
            L[elementI] = tmp2
            U[elementI] = tmp
            P[elementI] = column + 1

        for reihenElement in range(elementI + 1, n):
            try:
                multiplier = U[reihenElement][elementI] / U[elementI][elementI]
            except:
                multiplier = 0.

            for zeilenElement in range(elementI, n):
                U[reihenElement][zeilenElement] = U[reihenElement][zeilenElement] - multiplier * U[elementI][
                    zeilenElement]

            L[reihenElement][elementI] = multiplier

    for elementJ in range(n):
        L[elementJ][elementJ] = 1.

    return P, L, U


# noinspection PyPep8Naming
def prager_oettli(A, b, x):
    return b - np.dot(A, x), np.dot(np.absolute(A), np.absolute(x)) + np.absolute(b)


qs = [8, 10, 12]
for q in qs:
    print("10^-", q)
    delta = 1. / np.power(10, q)

    A = [[3., 2., 1.], [2., 2. * delta, 2. * delta], [1., 2. * delta, -1. * delta]]
    b = [3. + 3. * delta, 6. * delta, 2. * delta]

    P, L, U = pivot(A)

    x = permutation(P, b)
    x1 = vorwaerts(L, x)
    x2 = rueckwaerts(U, vorwaerts(L, x))
    print("x1 = ", x1)
    print("x2 = ", x2)

    # noinspection PyTypeChecker
    r, s = prager_oettli(A, b, x2)
    print("r = ", r)
    print("s = ", s)

    epsilon = 0
    # noinspection PyUnresolvedReferences
    while (np.absolute(r) > np.multiply(epsilon, s)).any():
        epsilon += 0.001
    print("Ab epsilon = ", epsilon, " gilt abs(r) <= epsilon * s ")
    print()
