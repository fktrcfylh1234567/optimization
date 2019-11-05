import matplotlib.pyplot as plt
import numpy

from lab1.opt_passive import opt_passive_method, get_number
from lab1.fibonacci import fibonacci_method, steps_count


def func(x):
    return -0.5 * numpy.cos(x * 0.5) + 1


a = -2.5
b = 1.5
e = 0.1

x = numpy.arange(a, b, 0.01)
y = func(x)

n = get_number(4, e)
opt_passive_min = opt_passive_method(func, a, b, n)

n = steps_count(4, e)
fibonacci_min = fibonacci_method(func, a, b, n)

lines = plt.plot(x, y, 'o')
plt.plot(opt_passive_min, func(opt_passive_min), 'o')
plt.plot(fibonacci_min, func(fibonacci_min), 'o')
plt.setp(lines[0], markersize=2)
plt.grid(True)
plt.show()
