import matplotlib.pyplot as plt
import numpy


def func(x):
    return -0.5 * numpy.cos(x * 0.5) + 1


a = -2.5
b = 1.5
e = 0.1

x = numpy.arange(a, b, 0.01)
y = func(x)

lines = plt.plot(x, y, 'o')
plt.setp(lines[0], markersize=2)
plt.grid(True)
plt.show()
