# Aufgabe 2
import math


def expo1(x, n):
    result = 0
    for k in range(0, n):
        result += (math.pow(x, k) / math.factorial(k))
    return result


def expo2(x, n):
    result = 0
    for k in range(0, n):
        result += (math.pow(x, n-k)/math.factorial(n-k))
    return result


print(expo1(3, 4))
print(expo2(3, 4))
print("e Funktion:")
print(math.pow(math.e, 4))
print()
print(expo1(44, 5))
print(expo2(44, 5))
print("e Funktion:")
print(math.pow(math.e, 5))
