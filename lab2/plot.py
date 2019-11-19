import matplotlib.pyplot as plt
import numpy
from lab2 import random_search, steps_count


def func_1(x):
    return -0.5 * numpy.cos(x * 0.5) + 1


def func_2(x):
    return func_1(x) * numpy.sin(5 * x)


a = -2.5
b = 1.5
x_min = 0
e = 0.1
d = e / 2
p = 0.95
l = b - a

x = numpy.arange(a, b, 0.001)
y1 = func_1(x)
y2 = func_2(x)

n = steps_count(l, e, p)
random_min_1 = random_search(func_1, a, b, n)

n = steps_count(l, e, p)
random_min_2 = random_search(func_2, a, b, n)

lines = plt.plot(x, y1, x, y2, 'o')
plt.setp(lines[0], markersize=2)
plt.setp(lines[1], markersize=2)
plt.plot(random_min_1, func_1(random_min_1), 'o')
plt.plot(random_min_2, func_2(random_min_2), 'o')
plt.grid(True)
plt.show()
