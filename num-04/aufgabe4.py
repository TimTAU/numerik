import numpy as np
import math


def householder(A):
    row_num = 0
    vectors = []
    for row in A:
        v = A[row_num:, row_num].copy()
        if len(v) == 1:
            break
        if v[0] >= 0:
            v[0] = v[0] + np.linalg.norm(v)
        else:
            v[0] = v[0] - np.linalg.norm(v)

        Q = calc_Q(v, row_num)
        A = Q.dot(A)
        vectors.append(v)
        row_num += 1

    d = A.diagonal().copy()
    row_num = 0
    for v in vectors:
        A[row_num:, row_num] = v
        row_num += 1

    return A, d


def calc_Q(v, row_num):
    I = np.identity(len(v))
    Q = I - (2 / math.pow(np.linalg.norm(v), 2)) * v[np.newaxis, :].T * v

    if len(Q) != len(A):
        I = np.identity(len(A))
        I[row_num:, row_num:] = Q
        Q = I.copy()

    return Q


def householder_solve(A, d, b):
    for i in range(0, len(d) - 1):
        v = A[i:, i].copy()
        Q = calc_Q(v, i)
        b = Q.dot(b)

    A = np.triu(A)
    np.fill_diagonal(A, d)

    x = np.linalg.solve(A, b)
    return x


def create_A(n):
    A = np.ones((n, n))

    iu1 = np.tril_indices(n, -1)
    iu2 = np.triu_indices(n, 1, n - 1)

    A[iu1] = -1
    A[iu2] = 0
    return A


def create_b(n):
    b = np.zeros((n, 1))
    for i in range(0, n - 1):
        b[i] = 3 - i

    b[n - 1] = 2 - n
    return b


A = np.array([[20, 18, 44], [0, 40, 45], [-15, 24, -108]])
b = np.array([[-4], [-45], [78]])

A, d = householder(A)
x = householder_solve(A, d, b)
print(x)

for i in range(40, 61, 10):
    A = create_A(i)
    b = create_b(i)
    A, d = householder(A)
    print(householder_solve(A, d, b))
    print(i)
