import numpy


def zerlegung(A):
    i = 0
    p = []
    row_length = len(A[0])
    for row in A:
        if i == row_length - 1:
            p.append(i)
            break
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
                l = int(row_to_change[i] / row[i])
            A[x][i] = l
            for index_element in range(i + 1, row_length):
                A[x][index_element] -= l * row[index_element]
        i += 1

    return A, p


def permutation(p, x):
    for i in range(0, len(x)):
        if p[i] != i:
            x[[i, i + 1]] = x[[i + 1, i]]
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


A = numpy.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]])
b = numpy.array([[3], [5], [4], [5]])
b = numpy.array([[4], [10], [12], [11]])

ret = zerlegung(A)
p = ret[1]
LU = ret[0]

x = permutation(p, b)
x = vorwaerts(LU, x)
x = rueckwaerts(LU, x)
print(x)
