import numpy


def matrix_a(n, beta):
    a = numpy.zeros((n, n))
    a[0][0] = 1
    a[0][n - 1] = beta
    a[n - 1][n - 2] = -beta
    for i in range(1, n - 1):
        a[i][i] = 1
        a[i][i - 1] = -beta

    return a


def vektor_b(n, beta):
    b = numpy.zeros(n)
    b[0] = 1 + beta
    b[n - 1] = -beta
    for i in range(1, n - 1):
        b[i] = 1 - beta

    return b


def zerlegung(A, mitPivot):
    i = 0
    p = []
    row_length = len(A[0])
    for row in A:
        if i == row_length - 1:
            p.append(i)
            break

        if (mitPivot):
            pivot = row[i]
            pivotRow = i
            for x in range(i + 1, row_length):
                if A[x][i] > pivot:
                    pivot = A[x][i]
                    pivotRow = x

            A[[i, pivotRow]] = A[[pivotRow, i]]
            p.append(pivotRow)
        else:
            if row[i] == 0:
                A[[i, i + 1]] = A[[i + 1, i]]
                p.append(i + 1)
            else:
                p.append(i)

        for x in range(i + 1, row_length):
            row_to_change = A[x]
            if row[i] == 0:
                l = 0
            else:
                l = row_to_change[i] / row[i]

            A[x][i] = l
            for index_element in range(i + 1, row_length):
                A[x][index_element] -= l * row[index_element]

        i += 1

    return A, p


def permutation(p, x):
    for i in range(0, len(x)):
        if p[i] != i:
            x[[i, p[i]]] = x[[p[i], i]]

    return x


def vorwaerts(LU, x):
    for i in range(1, len(x)):
        add = 0
        for y in range(0, i):
            add += LU[i][y] * x[y]

        x[i] = x[i] - add

    return x


def rueckwaerts(LU, x):
    for i in range(len(x) - 1, -1, -1):
        add = 0
        for y in range(len(x) - 1, i, -1):
            add += LU[i][y] * x[y]

        x[i] = (x[i] - add) / LU[i][i]

    return x


beta = 10
n = 20

A = matrix_a(n, beta)
b = vektor_b(n, beta)

LU, p = zerlegung(A, True)

x = permutation(p, b)
x = vorwaerts(LU, x)
x = rueckwaerts(LU, x)
print(x)
