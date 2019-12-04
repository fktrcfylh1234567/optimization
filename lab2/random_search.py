import random
from math import log

from prettytable import PrettyTable


def steps_count(l, e, p):
    return int(round(log(1 - p) / log(1 - e / l)))


def search(f, a, b, n):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["Step", "x", "y"]

    x_min = a
    f_min = f(a)
    for i in range(n):
        x = random.uniform(a, b)
        y = f(x)
        pretty_table.add_row([i + 1, round(x, 4), round(y, 4)])
        if y < f_min:
            x_min = x
            f_min = y

    print(pretty_table)
    return x_min
