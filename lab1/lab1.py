from math import cos

from opt_passive import opt_passive_method

from fibonacci import fibonacci_method


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
n = 13

x_min = fibonacci_method(func, a, b, n)
f_min = func(x_min)
print('fibonacci min x =', x_min)
print('fibonacci min f(x) =', f_min)
