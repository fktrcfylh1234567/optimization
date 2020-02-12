from copy import copy
from math import log
from lab2 import random_search


def filter_noise(y, r, e, p, x_max, x_min):
    a = search_weight(y, 0.5, e, p, x_max, x_min)
    print("a =", a)
    return filter_func(y, a, r)


def filter_func(f, a, r):
    for _ in range(r):
        filtered = copy(f)
        for i in range(len(f) - 1):
            filtered[i] = f[i - 1] * (1 - a) / 2 + f[i] * a + f[i + 1] * (
                        1 - a) / 2
        f = filtered

    return f


def search_weight(noise, weight, e, p, x_max, x_min):
    n = round(log(1 - p) / log(1 - e / (x_max - x_min)))
    return random_search.search(lambda x: j(noise, x, weight), 0, 1, n, False)


def pollution(f):
    max_diff = 0
    for i in range(len(f) - 1):
        dy = abs(f[i] - f[i - 1])
        if dy > max_diff:
            max_diff = dy
    return max_diff


def difference(noise, filtered):
    max_diff = 0
    for i in range(len(noise) - 1):
        dy = abs(noise[i] - filtered[i - 1])
        if dy > max_diff:
            max_diff = dy
    return max_diff


def j(f, a, weight):
    filtered = filter_func(f, a, 1)
    return weight * pollution(filtered) + (1 - weight) * difference(f, filtered)
