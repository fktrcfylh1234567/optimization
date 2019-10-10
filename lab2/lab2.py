from math import cos

from random_search import random_search

a = -2.5
b = 1.5


def func(x):
    return -0.5 * cos(x * 0.5) + 1


x_min = random_search(func, a, b, 29)

print(x_min)
