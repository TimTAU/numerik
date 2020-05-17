import numpy as np


def a_posteriori(f, x_start, alpha, s):
    alpha_schlange = alpha / (1 - alpha)
    print(alpha_schlange)

    iteration = 0
    diff = float("inf")
    while diff > s:
        if iteration != 0:
            x_start = x_k1

        x_k1 = f(x_start)
        print(x_k1)
        diff = alpha_schlange * abs(x_k1 - x_start)
        iteration += 1

    return iteration, diff


def x_k_plus_1(x_k):
    return (3 - np.log(x_k)) / (1 + (1 / x_k))


res = a_posteriori(x_k_plus_1, 1, 1 / 4,  1e-06)

print("Nach " + str(res[0]) + " Iterationen ist der Fehler " + str(res[1]) + " kleiner als die Schranke 1e-6")
