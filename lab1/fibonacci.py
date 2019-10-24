from math import sqrt
from prettytable import PrettyTable

pretty_table = PrettyTable()


def fibonacci_method(f, a, b, n):
    fn = fibonacci_number(n + 1)
    fn_prev = fibonacci_number(n)

    x1 = a + (fn - fn_prev) / fn * (b - a)
    x2 = a + fn_prev / fn * (b - a)

    for i in range(n):
        pretty_table.field_names = ["N", "a", "b", "x1", "x2"]
        pretty_table.add_row([i + 1, round(a, 4), round(b, 4), round(x1, 4), round(x2, 4)])
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = b - x1 + a
        else:
            b = x2
            x2 = x1
            x1 = b - x2 + a

    print(pretty_table)
    return (a + b) / 2


def steps_count(l, e):
    i = 2
    fn = l / e
    while fibonacci_number(i) < fn:
        i += 1
    return i


def fibonacci_number(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
