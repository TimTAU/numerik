import numpy
from numpy.linalg import cond, norm


# noinspection PyShadowingNames,PyPep8Naming
def zerlegung(A):
    n = len(A)
    U = A
    L_diagonal = numpy.eye(n)

    for col in range(0, n):
        L = numpy.eye(n)
        for row in range(col + 1, n):
            L[row][col] = -U[row][col] / U[col][col]

        U = numpy.matmul(L, U)
        # Invert L
        for row in range(col + 1, n):
            L[row][col] = -L[row][col]

        L_diagonal = numpy.matmul(L_diagonal, L)

    L = L_diagonal
    return L, U


# noinspection PyShadowingNames
def vorwaerts_einfuegen(A, b):
    n = len(A)
    x = numpy.zeros(n)
    for row in range(0, n):
        x[row] = (b[row] - numpy.sum(A[row] * x)) / A[row][row]

    return x


# noinspection PyShadowingNames
def rueckwaerts_einfuegen(A, b):
    n = len(A)
    x = numpy.zeros(n)
    for row in reversed(range(0, n)):
        x[row] = (b[row] - numpy.sum(A[row] * x)) / A[row][row]

    return x


# noinspection PyShadowingNames,PyPep8Naming
def hager(A):
    n = len(A)
    L, U = zerlegung(A)
    x = numpy.ones(n) / n
    kappa = norm(A, numpy.inf)

    while True:
        UT = numpy.transpose(U)
        v = vorwaerts_einfuegen(UT, x)
        LT = numpy.transpose(L)
        y = rueckwaerts_einfuegen(LT, v)

        xsi = numpy.sign(y)
        v = vorwaerts_einfuegen(L, xsi)
        z = rueckwaerts_einfuegen(U, v)

        if numpy.amax(z) <= numpy.dot(z, x):
            break

        j = numpy.where(z == numpy.amax(z))[0]
        x = numpy.zeros(n)
        x[j] = 1

    kappa_i = norm(y, 1)
    return kappa * kappa_i


for i in [8, 10, 12]:
    g = 10 ** -i
    print("Bei 10^", -i, ":", sep="")
    A = numpy.array([[3, 2, 1], [2, 2 * g, 2 * g], [1, 2 * g, -g]], dtype=float)
    h = hager(A)
    c = cond(A)
    print("Näherung = ", h)
    print("Exakte Lösung = ", c)
    print("Abweichung = ", h - c)
    print("----")

    # Keine Ahnung warum die Abweichung so riesig ist
