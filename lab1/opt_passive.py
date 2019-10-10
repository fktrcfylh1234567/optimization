from numpy import linspace


def opt_passive_method(f, a, b, n):
    x_prev = a
    f_prev = f(a)
    for x in linspace(a, b, num=n + 2, endpoint=True):
        fi = f(x)
        if fi > f_prev:
            return x_prev
        else:
            x_prev = x
            f_prev = fi
