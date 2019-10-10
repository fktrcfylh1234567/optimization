import unittest
from math import cos

from random_search import random_search, number


def func(x):
    return -0.5 * cos(x * 0.5) + 1


a = -2.5
b = 1.5
x_min = 0
e = 0.1
d = e / 2
p = 0.95


class MyTestCase(unittest.TestCase):
    def test_opt_passive(self):
        l = b - a
        n = number(l, e, p)
        print('N =', n)
        random_min = random_search(func, a, b, n)
        print(random_min)
        self.assertAlmostEqual(first=0, second=random_min, delta=d)


if __name__ == '__main__':
    unittest.main()
