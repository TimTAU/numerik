import numpy


def residuum(A, b, x):
    return b - numpy.dot(A, x)


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


# noinspection DuplicatedCode
def vorwaerts(LU, x):
    for i in range(1, len(x)):
        add = 0
        for y in range(0, i):
            add += LU[i][y] * x[y]

        x[i] = x[i] - add
    return x


# noinspection DuplicatedCode
def rueckwaerts(LU, x):
    for i in range(len(x) - 1, -1, -1):
        add = 0
        for y in range(len(x) - 1, i, -1):
            add += LU[i][y] * x[y]

        x[i] = (x[i] - add) / LU[i][i]

    return x


def solve(A, b):
    LU, p = zerlegung(A.copy(), True)

    bp = permutation(p, b.copy())
    y = vorwaerts(LU, bp)
    x = rueckwaerts(LU, y)

    print("zuvor")
    print(x)
    print("danach")

    rk = residuum(A, b, x)

    rkp = permutation(p, rk)
    z = vorwaerts(LU, rkp)
    pk = rueckwaerts(LU, z)

    x_new = x + pk

    return x_new

def create_A(n):
    A = numpy.eye(n)

    for i in range(0, n):
        A[i][n - 1] = 1

        for j in range(0, i):
            A[i][j] = -1

    return A


def create_b(n):
    b = numpy.zeros(n)
    for i in range(0, n - 1):
        b[i] = 2 - i

    b[n - 1] = 2 - n
    return b


# Aufgabe 2a)
for i in range(40, 61, 10):
    print("n=" + str(i))
    A = create_A(i)
    b = create_b(i)

    #print(solve(A, b))

def create_A2(n):
    A = numpy.eye(n)

    for i in range(1, n):
        for j in range(0, i):
            A[i][j] = i + j

    return A


def create_b2(n):
    b = numpy.zeros(n)
    b[0] = 1

    return b


# Aufgabe 2b)
for i in range(10, 16):
    print("n=" + str(i))
    A = create_A2(i)
    b = create_b2(i)

    print(solve(A, b))
