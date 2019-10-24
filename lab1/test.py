import unittest
from math import cos

from opt_passive import opt_passive_method, get_number
from fibonacci import fibonacci_method, steps_count


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
x_min = 0
e = 0.1
d = e / 2


class MyTestCase(unittest.TestCase):
    def test_opt_passive(self):
        print('Passive')
        n = get_number(4, e)
        print('N =', round(n))
        opt_passive_min = opt_passive_method(func, a, b, n)
        self.assertAlmostEqual(first=0, second=opt_passive_min, delta=d)

    def test_fibonacci(self):
        print('Fibonacci')
        n = steps_count(4, e)
        print('N =', round(n))
        fibonacci_min = fibonacci_method(func, a, b, n)
        self.assertAlmostEqual(first=0, second=fibonacci_min, delta=d)


if __name__ == '__main__':
    unittest.main()
