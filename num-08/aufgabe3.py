import numpy
import math


def f(x):
    return numpy.array([f1(x), f2(x)])


def f1(x):
    return math.sin(x[0]) - x[1]


def f2(x):
    return math.exp(-x[1]) - x[0]


def df(x):
    return numpy.array([[df1x(x), df1y(x)], [df2x(x), df2y(x)]])


def df1x(x):
    return math.cos(x[0])


def df1y(x):
    return -1


def df2x(x):
    return -1


def df2y(x):
    return -math.exp(-x[1])


xk = numpy.array([0, 0])
error = 1
i = 0
while(abs(error) > 1e-8):
    i = i + 1

    a = df(xk)
    b = f(xk)
    z = numpy.linalg.solve(a, b)

    xk1 = xk - z
    error = numpy.linalg.norm(xk) - numpy.linalg.norm(xk1)
    xk = xk1

print("Iterationen: " + str(i))
print("Nullstelle: " + str(xk))
