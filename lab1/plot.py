import pylab
import matplotlib.pyplot as plt
import numpy


def plot(foo, low, high, epsilon, extrs):
    x_list = numpy.arange(low, high, epsilon)
    y_list = [foo(x) for x in x_list]

    pylab.plot(x_list, y_list)
    for entry in extrs:
        pylab.plot(entry, foo(entry), 'o')
    plt.grid(True)
