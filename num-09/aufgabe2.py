import numpy
import math


# Das ganze hier könnte bestimmt optimiert werden indem Ergebnisse zwischengespeichert werden aber für diesen einfachen Fall soll diese Implementation reichen.


# A:
def calcD(points, n, m):
    if(n == m):
        return points[n][1]

    return (calcD(points, n, m + 1) - calcD(points, n - 1, m)) / (points[n][0] - points[m][0])


def calcYWithNewtonInterpolationRecursive(points, x, n, k):
    if(k == 0):
        return calcD(points, n, k)

    return calcD(points, n - k, 0) + ((x - points[n - k][0]) * calcYWithNewtonInterpolationRecursive(points, x, n, k - 1))


def calcYWithNewtonInterpolation(points, x):
    n = len(points) - 1
    return calcYWithNewtonInterpolationRecursive(points, x, n, n)


print("A)")
points = numpy.array([[0, 3], [1, 2], [3, 6]])
print(calcYWithNewtonInterpolation(points, 2))

# B:


def calcPointsB(m):
    points = numpy.zeros([m, 2])
    for i in range(m):
        x = -5 + (10 / (m - 1)) * i
        y = 1 / (1 + math.pow(x, 2))
        points[i] = [x, y]

    return points


def calcNewtonInterpolationRecursive(poitns, n, k):
    if(k == 0):
        return str(calcD(points, n, k))

    return str(calcD(points, n - k, 0)) + " + (x - " + str(points[n - k][0]) + ") * (" + calcNewtonInterpolationRecursive(points, n, k - 1) + ")"


def calcNewtonInterpolation(points):
    n = len(points) - 1
    return calcNewtonInterpolationRecursive(points, n, n)


print()
print("B)")
for i in [7, 9, 11]:
    points = calcPointsB(i)
    print("M: " + str(i))
    print("Polynom: " + calcNewtonInterpolation(points))
    print()

# C:


def calcPointsC(m):
    points = numpy.zeros([m, 2])
    for i in range(m):
        x = -5 * math.cos(math.pi * (((2 * i) + 1) / 2 * m))
        y = 1 / (1 + math.pow(x, 2))
        points[i] = [x, y]

    return points


print("C)")
for i in [7, 9, 11]:
    points = calcPointsC(i)
    print("M: " + str(i))
    print("Polynom: " + calcNewtonInterpolation(points))
    print()
