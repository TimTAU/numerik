import numpy as np
import math


def newton(f, df, x0):
    iteration = 0
    while abs(f(x0)) > np.finfo(np.float32).eps:
        x0 = x0 - (f(x0) / df(x0))
        iteration += 1

    return x0, iteration


def sekante(f, x_minus1, x0):
    iteration = 0
    while abs(f(x0)) > np.finfo(np.float32).eps:
        x_temp = x0
        x0 = x0 - ((x0 - x_minus1 )/ (f(x0) - f(x_minus1))) * f(x0)
        x_minus1 = x_temp
        iteration += 1

    return x0, iteration


a = 9.8606
c = -1.1085e25
d = 0.029
m = 9


def f_b(x):
    return a / (1 - c * np.exp(-d * x)) - m


def f_db(x):
    return -(a * c * d * np.exp(d * x)) / math.pow((np.exp(d * x) - c), 2)


newton_res = newton(f_b, f_db, 1961)
print(newton_res[0])
print(newton_res[1])

sekante_res = sekante(f_b, 1961, 2000)
print(sekante_res[0])
print(sekante_res[1])