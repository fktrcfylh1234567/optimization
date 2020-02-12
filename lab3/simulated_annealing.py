from math import exp
import random
from prettytable import PrettyTable


def search(f, a, b, d):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["T", "x", "f(x)", "Propability", "Reason"]

    t = 10000
    t_min = 0.1

    x = random.uniform(a, b)
    y = f(x)

    x_min = x
    y_min = y

    while t > t_min:
        x_new = random.uniform(x - d, x + d)

        if x_new < a:
            x_new = random.uniform(a, x + d)
        elif x_new > b:
            x_new = random.uniform(x - d, b)

        y_new = f(x_new)
        t *= 0.95

        if y_new < y:
            x = x_new
            y = y_new
            pretty_table.add_row([round(t, 4), round(x_new, 4), round(y_new, 4), 1, "Лучше"])
        else:
            propability = exp(-(y_new - y) / t)
            if random.uniform(0, 1) < propability:
                x = x_new
                y = y_new
                pretty_table.add_row([round(t, 4), round(x_new, 4), round(y_new, 4), round(propability, 4), "Случайно"])
            else:
                pretty_table.add_row([round(t, 4), round(x_new, 4), round(y_new, 4), round(propability, 4), "Игнор"])
                continue

        if y < y_min:
            x_min = x
            y_min = y

    print(pretty_table)
    return x_min
