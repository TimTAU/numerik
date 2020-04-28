import numpy


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


def permutationUm(p, x):
   # Transponieren in umgedrehter Reihenfolge
    for i in range(len(x) - 1, -1, -1):
        if p[i] != i:
            x[[i, p[i]]] = x[[p[i], i]]


def vorwaertsTrans(LU, c):
   # Löse trans(U)*v=c, wobei LU die normale LU-Zerlegung ist. U wird durch den Wechsel der Zeilen/Spaltenindizes "transponiert"
    for i in range(0, len(c)):
        add = 0
        for y in range(0, i):
            add += LU[y][i] * c[y]

        c[i] = (c[i] - add) / LU[i][i]


def rueckwaertsTrans(LU, v):
   # Löse trans(L)*w=v, wobei LU die normale LU-Zerlegung ist. L wird durch den Wechsel der Zeilen/Spaltenindizes "transponiert"
    for i in range(len(v) - 2, -1, -1):
        add = 0
        for y in range(len(v) - 1, i, -1):
            add += LU[y][i] * v[y]

        v[i] = v[i] - add


A = numpy.array([[0., 0., 0., 1.], [2., 1., 2., 0.],
                 [4., 4., 0., 0.], [2., 3., 1., 0.]])
b = numpy.array([152., 154., 56., 17.])

# Löse trans(A)*x=b über die normale LU-Zerlegung von A. Ein echtes Transponieren von L,U ist nicht nötig. Das wird durch das geschickte Tauschen von Zeilen/Spaltenindex gelöst/simuliert
LU, p = zerlegung(A, True)

vorwaertsTrans(LU, b)
rueckwaertsTrans(LU, b)
permutationUm(p, b)
print(b)
