from copy import copy


def filter(y, a, r):
    for i in range(r):
        filtered = copy(y)
        for i in range(len(y) - 1):
            filtered[i] = y[i - 1] * (1 - a) / 2 + y[i] * a + y[i + 1] * (1 - a) / 2
        y = filtered

    return y
