from math import cos

from lab2 import random_search, steps_count


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
x_min = 0
e = 0.1
d = e / 2
p = 0.95

length = b - a
n = steps_count(length, e, p)


def brute_force():
    fails_count = 0
    for i in range(10000):
        random_min = random_search(func, a, b, n)
        if abs(x_min - random_min) > d:
            fails_count += 1
    return fails_count / 100


fails_count_percent = brute_force()
print('fails in', fails_count_percent, '%')
