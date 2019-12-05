from math import exp
import random
from prettytable import PrettyTable


def search(f, a, b, d):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["T", "x", "y"]

    t = 10000
    t_min = 0.1

    x = random.uniform(a, b)
    y = f(x)

    x_min = x
    y_min = y

    while t > t_min:
        xi = random.uniform(x - d, x + d)

        if xi < a:
            xi = random.uniform(a, x + d)
        elif xi > b:
            xi = random.uniform(x - d, b)

        yi = f(xi)
        t *= 0.95

        pretty_table.add_row([round(t, 4), round(x, 4), round(y, 4)])

        if yi < y:
            x = xi
            y = yi
        elif random.uniform(0, 1) < exp(- (yi - y) / t):
            x = xi
            y = yi

        if y < y_min:
            x_min = x
            y_min = y

    print(pretty_table)
    return x_min
