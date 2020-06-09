import numpy as np
import math
from matplotlib import pyplot as plt

# Begin: Copy-Paste von aufgabe 3


def calcH(x):
    # Berechne den h-vektor auf basis der gegebenen x
    l = len(x) - 1
    h = np.zeros(l)
    for i in range(0, l):
        h[i] = x[i + 1] - x[i]

    return h


def calcGamma(y, h):
    # Berechne den gamma-vektor auf basis der gegebenen y und der berechneten h
    l = len(h) - 1
    g = np.zeros(l)
    for i in range(0, l):
        g[i] = 6 * ((y[i + 2] - y[i + 1]) /
                    h[i + 1] - (y[i + 1] - y[i]) / h[i])

    return g


def createMatrix(h):
   # Erstelle die h-matrix zum berechnen der betas.
    l = len(h) - 1
    a = np.zeros([l, l])
    for i in range(0, l):
        for j in range(0, l):
            if i == j:
                a[i][j] = 2*(h[i] + h[i + 1])
            elif j == i + 1:
                if j < l:
                    a[i][j] = h[j]
            elif j == i - 1:
                if j > -1:
                    a[i][j] = h[i]

    return a


def calcBeta(m, g):
    # Löse das LGS m*b=g um die betas zu berechnen und setze b0 und bn auf 0.
    z = np.linalg.solve(m, g)
    b = np.zeros(len(z) + 2)
    for i in range(1, len(z) + 1):
        b[i] = z[i-1]

    return b


def calcAlpha(y, h, b):
    # Berechne die alphas auf basis der gegebenen y, den berechneten h und den berechneten betas
    l = len(b)-1
    a = np.zeros(l)
    for i in range(0, l):
        a[i] = (y[i + 1] - y[i]) / h[i] - 1. / 3 * \
            b[i] * h[i] - 1. / 6 * b[i + 1] * h[i]

    return a


def evalSingleSplineFunction(x, y, h, a, b, i, z):
    # Evaluiert die einzelne Splinefunktion pi(z) an position z (nicht schön, aber funktioniert)
    c = z - x[i]

    d = y[i]

    e = a[i]
    f = e * c

    r = b[i] / 2
    s = math.pow(c, 2)
    t = r * s

    l = (b[i + 1] - b[i]) / (6 * h[i])
    v = l * math.pow(c, 3)

    return d + f + t + v


def createSingleSplineFunction(x, y, h, a, b, i):
    # Erstelle ein lambda um die einzelne Splinefunktion pi(z) zu repräsentieren
    return lambda z: evalSingleSplineFunction(x, y, h, a, b, i, z)


def createSpline(x, y, h, a, b):
    # Erstelle eine Liste der einzelnen Splinefunktionen
    funcs = []
    for i in range(0, len(x) - 1):
        funcs.append(createSingleSplineFunction(x, y, h, a, b, i))

    # Return ein lamda das den Spline and einer Position z auswertet
    return lambda z: evalSpline(x, funcs, z)


def evalSpline(x, funcs, z):
    # Evaluiere den Spline an Position z, indem das passende Intervall gesucht wird und die entsprechende einzelne Splinefunktion an z ausgewertet wird
    if z < x[0]:
        return funcs[0](z)

    for i in range(1, len(x)):
        if z <= x[i]:
            return funcs[i - 1](z)

    return funcs[len(funcs) - 1](z)


def calcSpline(x, y):
    # Berechne den Spline
    h = calcH(x)
    g = calcGamma(y, h)
    m = createMatrix(h)
    b = calcBeta(m, g)
    a = calcAlpha(y, h, b)
    return createSpline(x, y, h, a, b)

# Ende: Copy-Paste von aufgabe 3


def gx(t):
    return 1. / (1 + t) * math.cos(3 * math.pi * t)


def gy(t):
    return 1. / (1 + t) * math.sin(3 * math.pi * t)


def calcPoints(m):
    points = np.zeros([3, m])
    for i in range(m):
        t = i / (m - 1.)
        x = gx(t)
        y = gy(t)
        points[0][i] = t
        points[1][i] = x
        points[2][i] = y

    return points


# Berechne die eigentlichen Funktionswerte
t = np.arange(0, 1, 0.01)
x = []
y = []
for i in t:
    x.append(gx(i))
    y.append(gy(i))

for m in [7, 9, 11]:
    # Plotte die original Funktion in blau
    plt.plot(x, y, 'b')

    # Berechne die Stützstellen und werte die original Funktion dort aus
    a = calcPoints(m)
    e = a[0]  # stützstellen
    f = a[1]  # x and den stützstellen ausgewertet
    g = a[2]  # y and den stützstellen ausgewertet

    # Berechne jeweils einen Spline für x und einen für y
    splineX = calcSpline(e, f)
    splineY = calcSpline(e, g)

    # Werte den Spline an den gleichen Stellen wie die eigentliche Funktion aus
    v = []  # splineX ausgewertet
    w = []  # splineY ausgewertet
    for i in t:
        v.append(splineX(i))
        w.append(splineY(i))

    # Plotte den Graphen der Splines in grün
    plt.plot(v, w, 'g')
    plt.title("Original blau, Spline grün (m = " + str(m) + ")")
    plt.show()
