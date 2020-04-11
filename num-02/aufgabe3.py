import numpy
import math


def matrix_a(n):
    a = numpy.zeros((n, n))
    numpy.fill_diagonal(a, 2)
    for i in range(0, n - 1):
        a[i + 1][i] = -1

    return a


def vektor_b(n):
    b = [-1. / math.pow((n + 1), 2)] * n
    return b


def cholesky_spezial(A):
    vektor1 = numpy.copy(numpy.diagonal(A))
    vektor2 = numpy.copy(numpy.diagonal(A, -1))

    for i in range(0, len(vektor2)):
        vektor1[i] = math.sqrt(vektor1[i])
        A[i][i] = vektor1[i]
        vektor2[i] = vektor2[i] / vektor1[i]
        A[i + 1][i] = vektor2[i]
        vektor1[i + 1] = vektor1[i + 1] - math.pow(vektor2[i], 2)
        A[i + 1][i + 1] = vektor1[i + 1]

    vektor1[len(vektor1) - 1] = math.sqrt(vektor1[len(vektor1) - 1])
    A[len(vektor1) - 1][len(vektor1) - 1] = vektor1[len(vektor1) - 1]

    return [vektor1, vektor2]


def cholesky_zerlegung(A, b):
    y = numpy.linalg.solve(A, b)
    x = numpy.linalg.solve(numpy.transpose(A), y)

    return x


A = matrix_a(100)
vektor1, vektor2 = cholesky_spezial(A)
b = vektor_b(100)
print(cholesky_zerlegung(A, b))
A = matrix_a(1000)
vektor1, vektor2 = cholesky_spezial(A)
b = vektor_b(1000)
print(cholesky_zerlegung(A, b))
A = matrix_a(10000)
vektor1, vektor2 = cholesky_spezial(A)
b = vektor_b(10000)
print(cholesky_zerlegung(A, b))
