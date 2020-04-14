import numpy
import math


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


def loese_mitLU(LU, p, b):
    x = permutation(p, b)
    x = vorwaerts(LU, x)
    x = rueckwaerts(LU, x)
    return x


def simple_matrix_product(vector1, vector2):
    product = 0.
    for i in range(0, len(vector1)):
        product += vector1[i]*vector2[i]
    return product


def multiply(factor, vector):
    for i in range(0, len(vector)):
        vector[i] *= factor
    return vector


def subtract(vector1, vector2):
    for i in range(0, len(vector1)):
        vector1[i] -= vector2[i]
    return vector1


# Matrizen und Vektoren definieren
A = numpy.array([[0., 0., 0., 1.], [2., 1., 2., 0.],
                 [4., 4., 0., 0.], [2., 3., 1., 0.]])
u = numpy.array([0., 1., 2., 3.])
v = numpy.array([0., 0., 0., 1.])

A2 = numpy.array([[0., 0., 0., 1.], [2., 1., 2., 1.],
                  [4., 4., 0., 2.], [2., 3., 1., 3.]])
b2 = numpy.array([3., 5., 4., 5.])

# LU-Zerlegung von A und Az=u lösen
LU, p = zerlegung(A)
z = numpy.copy(u)
z = loese_mitLU(LU, p, z)

# Schauen ob A regulär ist und a ausrechnen
matrixProduct = simple_matrix_product(v, z)
temp = 1 + matrixProduct
if(math.isclose(temp, 0)):
    exit()

a = 1. / temp

# Az2=b2 lösen
z2 = loese_mitLU(LU, p, b2)

# x2 lösen
matrixProduct = simple_matrix_product(v, z2)
z = multiply(matrixProduct, z)
x2 = subtract(z2, z)
print(x2)
