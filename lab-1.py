from math import cos

from numpy import linspace


def opt_passive(a, b, n):
    x_prev = a
    f_prev = f(a)
    for x in linspace(a, b, num=n + 2, endpoint=True):
        fi = f(x)
        if fi > f_prev:
            return x_prev
        else:
            x_prev = x
            f_prev = fi


def f(x):
    return -0.5 * cos(x * 0.5) + 1


x_min = opt_passive(-2.5, 1.5, 29)
f_min = f(x_min)
print('min x =', x_min)
print('min f(x) =', f_min)
