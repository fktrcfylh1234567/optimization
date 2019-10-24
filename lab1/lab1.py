from math import cos

from fibonacci import fibonacci_method, steps_count


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
e = 0.1

n = steps_count(b - a, e)
print('N =', n)

x_min = fibonacci_method(func, a, b, n)
f_min = func(x_min)
print('fibonacci min x =', x_min)
print('fibonacci min f(x) =', f_min)
