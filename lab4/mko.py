from copy import copy

import matplotlib.pyplot as plt
import numpy as np


def main_criteria(choices, main, limits):
    maximums = list(max(choices, key=lambda a: a[i])[i] for i in range(4) if i != main)
    limits_num = list(maximums[i] * limits[i] for i in range(3))
    limits_num.insert(main, None)

    filtered = copy(choices)
    for i in (i for i in range(4) if i != main):
        filtered = list(filter(lambda it: it[i] > limits_num[i], filtered))

    opt_choice = choices.index(max(filtered, key=lambda a: a[main]))
    return opt_choice


def pareto(choices, main_x, main_y, labels):
    for i in range(4):
        plt.plot(choices[i][main_x], choices[i][main_y], 'o', label=labels[i])
    plt.grid(True)
    plt.legend()
    plt.show()

    return choices.index(max(choices, key=lambda a: a[main_x] ** 2 + a[main_y] ** 2))


def convolution(choices, weights):
    choices = np.array(choices)
    weights = np.array(weights)

    choices_sum = np.abs(choices).sum(axis=0)
    weights_sum = np.abs(weights).sum(axis=0)

    choices = choices / choices_sum
    weights = weights / weights_sum

    res = np.dot(choices, weights)
    return np.where(res == np.amax(res))[0][0]


def saaty(choices, weights):
    choices = [[sum(choices[i][cr] / choices[j][cr] for j in range(4)) for i in range(4)] for cr in range(4)]
    choices = np.array(choices).transpose()
    choices = choices / np.abs(choices).sum(axis=0)

    weights = [sum(weights[i] / weights[j] for j in range(4)) for i in range(4)]
    weights = np.array(weights).transpose()
    weights = weights / np.abs(weights).sum(axis=0)

    res = np.dot(choices, weights)
    return np.where(res == np.amax(res))[0][0]
