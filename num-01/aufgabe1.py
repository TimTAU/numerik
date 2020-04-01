# Aufgabe 1
import math


def pq1(p, q):
    x1 = -p + math.sqrt((math.pow(p, 2) + q))
    x2 = -p - math.sqrt((math.pow(p, 2) + q))
    return x1, x2


def pq2(p, q):
    x1 = -p - math.sqrt(math.pow(p, 2) + q)
    x2 = -p / x1
    return x1, x2


def printpqs(p, q):
    print(pq1(p, q))
    print(pq2(p, q))


print("p = 10^2, q = 1")
print(printpqs(math.pow(10, 2), 1))
print()
print("p = 10^4, q = 1")
print(printpqs(math.pow(10, 4), 1))
print()
print("p = 10^6, q = 1")
print(printpqs(math.pow(10, 6), 1))
print()
print("p = 10^7, q = 1")
print(printpqs(math.pow(10, 7), 1))
print()
print("p = 10^8, q = 1")
print(printpqs(math.pow(10, 8), 1))

"""
Zweites Verfahren ist genauer
"""