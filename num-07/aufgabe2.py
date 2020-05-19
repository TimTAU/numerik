import math
from numpy import finfo

a = 9.8606
c = -1.1085e25
d = 0.029


def evalFunc(x):
    return a / (1 - c * math.exp(-d * x)) - 9


def evalFirstDerivative(x):
    return -a * c * d * math.exp(d * x) / math.pow(math.exp(d * x) - c, 2)


def newton(x):
    return x - (evalFunc(x) / evalFirstDerivative(x))


def sekante(xk, xk1, prevEval):
    z = evalFunc(xk1)
    return xk1 - (xk1 - xk) / (z - prevEval) * z, z


# Newton-Verfahren:
i = 0
xk = 0
xk1 = 1961
# Das Verfahren hat bei mir im gegensatz zum Sekantenverfahren niemals Maschinengenauigkeit erreicht. Deswegen hier eine leicht kleinere Zahl als Abbruch.
while(abs(xk - xk1) > 1e-12):
    i = i + 1
    xk = xk1
    xk1 = newton(xk)

print("Ergebnis nach Newton: " + str(xk1))
print("Iterationen Newton: " + str(i))
print()

# Sekantenverfahren:
i = 0
xk = 0
xk1 = 1961
xk2 = 2000
prevEval = evalFunc(xk1)
while(abs(xk2 - xk1) > finfo(float).eps):
    i = i + 1
    xk = xk1
    xk1 = xk2
    xk2, prevEval = sekante(xk, xk1, prevEval)

print("Ergebnis nach Sekantenverfahren: " + str(xk2))
print("Iterationen Sekantenverfahren: " + str(i))
