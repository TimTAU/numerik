# Aufgabe 4
import math

import numpy

function1 = lambda x: 1 / math.pow(x, 2)

function2 = lambda x: math.log(x)


def trapez(a, b, n):
    h = (b - a) / n
    result = []
    for i in range(1, n - 1):
        result.append(a + i * h)
    return result


def trapez_result_function1():
    h = (10 - 1 / 10) / 100
    vector = numpy.array(trapez(1 / 10, 10, 100))
    f1 = numpy.vectorize(function1)
    result = f1(vector)
    return (h / 2) * (function1(1 / 10) + 2 * sum(result) + function1(10))


def trapez_result_function2():
    h = (2 - 1) / 100
    vector = numpy.array(trapez(1, 2, 100))
    f2 = numpy.vectorize(function2)
    result = f2(vector)
    return (h / 2) * (function2(1) + 2 * sum(result) + function2(2))


print(trapez_result_function1())
print(trapez_result_function2())
