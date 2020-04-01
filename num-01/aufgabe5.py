# Aufgabe 5
import math


def a_k(k):
    if k == 0:
        return math.sqrt(x0)
    return ((3 / 2 * k) - 1) * ((x / x0) - 1) * a_k(k - 1)


def y_k(k):
    if k == 0:
        return math.sqrt(x0)
    return y_k(k - 1) + a_k(k)


def heron(k):
    if k == 0:
        return math.sqrt(x0)
    return 1 / 2 * (heron(k - 1) + (x / (heron(k - 1))))


x = 2
x0 = 1
print("y_k:")
print(y_k(1))
print("Heron:")
print(heron(1))
print("Exakte Wurzel:")
print(math.sqrt(2))
print("-----")


counter = 1
while (x - math.sqrt(2)) > 0.005:
    x = heron(counter)
    counter += 1
print("Nach ", counter, " Iterationen ist die Differenz kleiner als Heron (0.005)")
