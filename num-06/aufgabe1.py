import math

import numpy


def cg(x0, eps=1e-6):
    xk = x0.copy()
    rk = b - A.dot(xk)
    pk = rk.copy()

    rknrkn = rk.dot(rk)
    res = [math.sqrt(rknrkn)]

    r0r0 = rknrkn

    while rknrkn > eps * 2 * r0r0:
        Apk = A.dot(pk)
        rkrk = rknrkn
        alpha = rkrk / pk.dot(Apk)

        xk += alpha * pk
        rk -= alpha * Apk

        rknrkn = rk.dot(rk)
        beta = rknrkn / rkrk

        pk = rk + beta * pk

        res.append(math.sqrt(rknrkn))

    return xk, numpy.array(res) / math.sqrt(r0r0)


for m in [50, 100, 200]:
    A, b = system(m)

    n = m * m
    x0 = numpy.zeros(n)
    plotxk
