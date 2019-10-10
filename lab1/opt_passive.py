from numpy import linspace


def get_number(l, e):
    return 2 * l / e + 1


def opt_passive_method(f, a, b, n):
    x_prev = a
    f_prev = f(a)
    for x in linspace(a, b, num=n + 2):
        fi = f(x)
        print('x =', x, 'y =', fi)
        if fi > f_prev:
            return x_prev
        else:
            x_prev = x
            f_prev = fi
