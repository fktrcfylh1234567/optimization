import unittest
from math import cos

from opt_passive import opt_passive_method
from fibonacci import fibonacci_method


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
n = 29


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass
        opt_passive_min = opt_passive_method(func, a, b, n)
        fibonacci_min = fibonacci_method(func, a, b, n)
        self.assertAlmostEqual(first=0, second=opt_passive_min, delta=0.1)
        self.assertAlmostEqual(first=0, second=fibonacci_min, delta=0.001)


if __name__ == '__main__':
    unittest.main()
