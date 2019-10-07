from math import cos

from fibonacci import fibonacci_method
from opt_passive import opt_passive_method


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
n = 29

x_min = opt_passive_method(func, a, b, n)
f_min = func(x_min)
print('opt_passive min x =', x_min)
print('opt_passive min f(x) =', f_min)

x_min = fibonacci_method(func, a, b, n)
f_min = func(x_min)
print('fibonacci min x =', x_min)
print('fibonacci min f(x) =', f_min)
