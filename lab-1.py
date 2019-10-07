from math import cos

from fibonacci import fibonacci_method
from opt_passive import opt_passive_method


def func(x):
    return -0.5 * cos(x * 0.5) + 1


x_min = opt_passive_method(func, -2.5, 1.5, 29)
f_min = func(x_min)
print('min x =', x_min)
print('min f(x) =', f_min)

x_min = fibonacci_method(func, -2.5, 1.5, 29)
f_min = func(x_min)
print('min x =', x_min)
print('min f(x) =', f_min)
