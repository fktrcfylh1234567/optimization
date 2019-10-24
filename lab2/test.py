import unittest
import numpy
from random_search import random_search, steps_count


def func_1(x):
    return -0.5 * numpy.cos(x * 0.5) + 1


def func_2(x):
    return func_1(x) * numpy.sin(5 * x)


a = -2.5
b = 1.5
x_min_1 = 0
x_min_2 = -1.582
e = 0.1
d = e / 2
p = 0.95
l = b - a


class MyTestCase(unittest.TestCase):
    def test_opt_passive_uni(self):
        n = steps_count(l, e, p)
        print('N =', n)
        random_min = random_search(func_1, a, b, n)
        print(random_min)
        self.assertAlmostEqual(first=x_min_1, second=random_min, delta=d)

    def test_opt_passive_multi(self):
        n = steps_count(l, e, p)
        print('N =', n)
        random_min = random_search(func_2, a, b, n)
        print(random_min)
        self.assertAlmostEqual(first=x_min_2, second=random_min, delta=d)


if __name__ == '__main__':
    unittest.main()
