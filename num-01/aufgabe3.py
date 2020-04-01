# Aufgabe 3
import math

from scipy import integrate


def recsum(f, a, b, n):
    result = 0
    h = (b - a / n)
    for i in range(1, n):
        result += f(a + i * h)
    return h * result


def traprule(f, a, b, n):
    result = 0
    h = (b - a / n)
    for i in range(1, n - 1):
        result += f(a + i * h)
    return h / 2 * (f(a) + 2 * result + f(b))


def func1(x):
    return 1 / math.pow(x, 2)


def func2(x):
    return math.log(x)


print("Funktion 1")
print(recsum(func1, 1 / 10, 10, 20))
print(traprule(func1, 1 / 10, 10, 20))
print(integrate.quad(func1, 1 / 10, 10))
print()
print("Funktion 2")
print(recsum(func2, 1, 2, 20))
print(traprule(func2, 1, 2, 20))
print(integrate.quad(func2, 1, 2))
