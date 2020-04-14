import numpy
import math


def matrix_a(n):
    a = numpy.zeros((n, n))
    for i in range(0, n):
        a[i][i] = 2
        if i != 0:
            a[i - 1][i] = -1
        if i != n - 1:
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


def loese(vektor1, vektor2, b):
    for i in range(0, len(vektor1)):
        if i == 0:
            b[i] = b[i] / vektor1[i]
        else:
            b[i] = (b[i] - vektor2[i - 1] * b[i - 1]) / vektor1[i]

    for i in range(len(vektor1) - 1, -1, -1):
        if i == n - 1:
            b[i] = b[i] / vektor1[i]
        else:
            b[i] = (b[i] - vektor2[i] * b[i + 1]) / vektor1[i]


def cholesky_zerlegung(A, b):
    y = numpy.linalg.solve(A, b)
    x = numpy.linalg.solve(numpy.transpose(A), y)
    return x


n = 1000
A = matrix_a(n)
b = vektor_b(n)

vektor1, vektor2 = cholesky_spezial(A)
loese(vektor1, vektor2, b)
print(b)
