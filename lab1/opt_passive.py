from numpy import linspace
from prettytable import PrettyTable

pretty_table = PrettyTable()


def get_number(l, e):
    return 2 * l / e + 1


def opt_passive_method(f, a, b, n):
    x_prev = a
    f_prev = f(a)
    for x in linspace(a, b, num=round(n + 2)):
        fi = f(x)
        pretty_table.field_names = ["x", "f(x)"]
        pretty_table.add_row([round(x, 4), round(fi, 4)])
        if fi > f_prev:
            print(pretty_table)
            return x_prev
        else:
            x_prev = x
            f_prev = fi
