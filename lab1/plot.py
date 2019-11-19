import matplotlib.pyplot as plt
import numpy

from lab1.fibonacci import fibonacci_method, steps_count_fib
from lab1.opt_passive import steps_count_opt, opt_passive_method


def func(x):
    return -0.5 * numpy.cos(x * 0.5) + 1


def calculate(f, a, b, e):
    x = numpy.arange(a, b, 0.01)
    y = f(x)

    n = steps_count_opt(4, e)
    opt_passive_min = opt_passive_method(f, a, b, n)

    n = steps_count_fib(4, e)
    fibonacci_min = fibonacci_method(f, a, b, n)

    lines = plt.plot(x, y, 'o')
    plt.plot(opt_passive_min, f(opt_passive_min), 'o')
    plt.plot(fibonacci_min, f(fibonacci_min), 'o')
    plt.setp(lines[0], markersize=2)
    plt.grid(True)
    plt.show()


calculate(func, -2.5, 1.5, 0.1)
