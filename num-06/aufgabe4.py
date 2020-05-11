import numpy
import math
from Blatt06_lib import Ablock, plotev, animev


def sign(t):
    if t < 0:
        return -1
    else:
        return 1


def calcAlpha(A, j, i):
    return (A[j][j] - A[i][i]) / (2 * A[i][j])


def calcC(alpha):
    oneHalf = 1 / 2.
    return math.sqrt(oneHalf + oneHalf * math.sqrt(math.pow(alpha, 2) / (1 + math.pow(alpha, 2))))


def calcS(c, alpha):
    return sign(alpha) / (2 * c * math.sqrt(1 + math.pow(alpha, 2)))


def getBiggestElement(A):
    a = 0
    b = 0
    biggestElement = 0.0
    for j in range(1, len(A)):
        for i in range(0, j):
            if j == 1 and i == 0 or abs(A[i][j]) > biggestElement:
                biggestElement = abs(A[i][j])
                a = i
                b = j

    return a, b


def getQuadratSum(A):
    sum = 0.0
    for j in range(1, len(A)):
        for i in range(0, j):
            sum += 2 * math.pow(A[i][j], 2)

    return sum


def calCurrentP(A):
    i, j = getBiggestElement(A)
    alpha = calcAlpha(A, i, j)
    c = calcC(alpha)
    s = calcS(c, alpha)
    p = numpy.identity(len(A))
    p[i][i] = c
    p[i][j] = -s
    p[j][i] = s
    p[j][j] = c

    return p


m = 10
A = Ablock(m)
q = numpy.identity(m * m)
#A = numpy.array([[1, 1/2., 1/3.], [1/2., 1/3., 1/4.], [1/3., 1/4., 1/5.]])
#q = numpy.identity(3)

i = 1
sum = getQuadratSum(A)
while sum > math.pow(10, -3):
    i += 1
    p = calCurrentP(A)
    A = p.T.dot(A.dot(p))
    sum = getQuadratSum(A)
    q = q.dot(p)

print("Iterationen: " + str(i))
print(A)
print(q)

index1 = 0
index2 = 0
index3 = 0
index4 = 0
for i in range(1, len(A)):
    currentIndex = i
    if A[currentIndex][currentIndex] < A[index1][index1]:
        temp = index1
        index1 = currentIndex
        currentIndex = temp

    if A[currentIndex][currentIndex] < A[index2][index2]:
        temp = index2
        index2 = currentIndex
        currentIndex = temp

    if A[currentIndex][currentIndex] < A[index3][index3]:
        temp = index3
        index3 = currentIndex
        currentIndex = temp

    if A[currentIndex][currentIndex] < A[index4][index4]:
        temp = index4
        index4 = currentIndex
        currentIndex = temp

plotev(q[index1])
plotev(q[index2])
plotev(q[index3])
plotev(q[index4])
