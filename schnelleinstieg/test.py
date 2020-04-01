from pylab import *

l1 = list(range(6))
print(l1)

x = linspace(0, 1, 20)
y = linspace(0, 2, 30)
yy, xx = meshgrid(y, x)


def f(x, y):
    return y ** 2 * sin(2. * pi * x)


fig = figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, f(xx, yy), cmap=cm.jet, rstride=1, cstride=1)
