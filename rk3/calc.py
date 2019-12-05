import numpy

from rk3 import genetic_algorithm, plot


def func(x, y):
    return -numpy.sqrt(numpy.log(1 + x ** 2 + y ** 2))


x, y = genetic_algorithm.search(func, -1, 1, -1, 1)
plot.make_plot(func, -1, 1, -1, 1, x, y, func(x, y))
