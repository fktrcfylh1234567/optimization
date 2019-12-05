from math import sqrt, log

from rk3 import genetic_algorithm


def func(x, y):
    return -sqrt(log(1 + x ** 2 + y ** 2))


genetic_algorithm.search(func, -1, 1, -1, 1)
